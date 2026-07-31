import os, shutil, subprocess
import tqdm

def mp4_to_wav_ffmpeg(mp4_path, wav_path):
    """
    用 ffmpeg 命令行将 mp4 转为 wav
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-v", "quiet",
        "-i", mp4_path,        
        "-vn",                 
        "-acodec", "pcm_s16le",
        wav_path
    ]
    subprocess.run(cmd, check=True)

gt_data_file = "data/test_files/PlanAudio-Bench"
target_dir = "<path of generated audio>"
target_wav_dir = "<path of gt audio>"

os.makedirs(target_dir, exist_ok=True)
os.makedirs(target_wav_dir, exist_ok=True)

with open(gt_data_file, 'r') as file:
    for line in tqdm.tqdm(file.readlines()):
        basename, wav_path, audio_caption, speech_trans, prompt = line.strip().split("\t")
        if not os.path.exists(f"{target_dir}/{basename}.mp4"):
            shutil.copy(wav_path, f"{target_dir}/{basename}.mp4")
        mp4_to_wav_ffmpeg(f"{target_dir}/{basename}.mp4", f"{target_wav_dir}/{basename}.wav")
