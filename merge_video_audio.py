import os
from moviepy.editor import VideoFileClip, AudioFileClip
from multiprocessing.pool import ThreadPool

def merge_video_audio(video_filename, audio_filename, output_filename):
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 构建完整的文件路径
    video_path = os.path.join(current_directory, video_filename)
    audio_path = os.path.join(current_directory, audio_filename)
    output_path = os.path.join(current_directory, output_filename)

    # 读取视频和音频文件
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # 将音频与视频合并
    video_clip = video_clip.set_audio(audio_clip)

    # 保存合并后的视频
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# 获取当前文件夹中的视频和音频文件列表
video_files = [f for f in os.listdir() if f.endswith('.mp4')]
audio_files = [f for f in os.listdir() if f.endswith('.mp3')]

# 确保只使用第一个找到的视频和音频文件
if video_files and audio_files:
    video_filename = video_files[0]
    audio_filename = audio_files[0]
    
    # 构建输出文件名
    output_filename = f"output_{video_filename}"

    # 使用 ThreadPool 进行并发处理
    pool = ThreadPool()
    result = pool.apply_async(merge_video_audio, (video_filename, audio_filename, output_filename))
    result.get()  # 等待并获取结果
else:
    print("未找到视频或音频文件。")
