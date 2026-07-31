#!/bin/bash
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1

device=1

models=(
    ""
)
pred_path="<path of generated audio>"

setting=mix
if [[ "$setting" == "audio" ]]; then
    gt_audio="<path of gt audio>"
    cache_path="<path of cache>"
fi
if [[ "$setting" == "mix" ]]; then
    gt_audio="<path of gt audio>"
    cache_path="<path of cache>"
fi

for i in "${models[@]}"; do
    echo "Running: $i"
    CUDA_VISIBLE_DEVICES=${device} python evaluate.py \
    --gt_audio ${gt_audio} \
    --gt_cache ${cache_path}/gt_cache \
    --pred_audio ${pred_path} \
    --pred_cache ${cache_path}/${i} \
    --audio_length=10 \
    --recompute_pred_cache \
    --skip_video_related
done