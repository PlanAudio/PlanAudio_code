import os, glob
import pdb

text_file = "<path of test file>"
data_list = []
with open(text_file, 'r') as file:
    for line in file.readlines():
        basename, wav_path, audio_caption, speech_trans, prompt = line.strip().split("\t")
        data_list.append((basename, speech_trans))

cache_dir = "<path of cache>"

# scp file gt.scp & gen.scp
gt_dir = "<path of gt audio>"
gen_dir = "<path of generated audio>"
exp_name = ""
cache_path = f"{cache_dir}/{exp_name}"
os.makedirs(cache_path, exist_ok=True)

gt_list = []
gen_list = []
text_list = []
if os.path.exists(f"{cache_dir}/gt/test.scp"):
    pass
else:
    for (basename, text) in data_list:
        if os.path.exists(f"{gt_dir}/{basename}.wav") and os.path.exists(f"{gen_dir}/{basename}.wav"):
            gt_list.append((basename, f"{gt_dir}/{basename}.wav"))
            gen_list.append((basename, f"{gen_dir}/{basename}.wav"))
            text_list.append((basename, text))

with open(f"{cache_path}/gt.scp", 'w') as file:
    for item in gt_list:
        file.write(f"{item[0]} {item[1]}\n")

with open(f"{cache_path}/gen.scp", 'w') as file:
    for item in gen_list:
        file.write(f"{item[0]} {item[1]}\n")

with open(f"{cache_path}/text", 'w') as file:
    for item in text_list:
        file.write(f"{item[0]} {item[1]}\n")







