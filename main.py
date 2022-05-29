from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import timedelta

SAVING_FRAMES_PER_SECOND = 15

def format_timedelta(td):
    """Служебная функция для классного форматирования объектов timedelta (например, 00: 00: 20.05)
    исключая микросекунды и сохраняя миллисекунды"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def main(video_file):
    # загрузить видеоклип
    video_clip = VideoFileClip(video_file)
    # создаем папку по названию видео файла
    filename, _ = os.path.splitext(video_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # если SAVING_FRAMES_PER_SECOND выше видео FPS, то установите его на FPS (как максимум)
    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    # если SAVING_FRAMES_PER_SECOND установлен в 0, шаг равен 1 / fps, иначе 1 / SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    # перебираем каждый возможный кадр
    for current_duration in np.arange(0, video_clip.duration, step):
        # отформатируйте имя файла и сохраните его
        frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
        frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")
        # сохраняем кадр с текущей длительностью
        video_clip.save_frame(frame_filename, current_duration)

if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)