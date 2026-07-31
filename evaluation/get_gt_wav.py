import os, shutil, subprocess
import tqdm

gt_data_file = "data/test_files/PlanAudio-Bench"
target_wav_dir = "<path of generated audio>"
os.makedirs(target_wav_dir, exist_ok=True)

with open(gt_data_file, 'r') as file:
    for line in tqdm.tqdm(file.readlines()):
        basename, wav_path, audio_caption, speech_trans, prompt = line.strip().split("\t")
        if not os.path.exists(f"{target_wav_dir}/{basename}.wav"):
            shutil.copy(wav_path, f"{target_wav_dir}/{basename}.wav")
