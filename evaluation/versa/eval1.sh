#!/bin/bash

export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1

device=0

models=(
    ""
)
setting=mix

if [[ "$setting" == "mix" ]]; then
    path="<path of cache>"
fi
if [[ "$setting" == "speech" ]]; then
    path="<path of cache>"
fi

for cmd in "${commands[@]}"; do
    echo "Running: $cmd"
    CUDA_VISIBLE_DEVICES=${device} python -W ignore::UserWarning versa/bin/scorer.py \
    --score_config evaluation/versa/egs/separate_metrics/mix.yaml \
    --gt ${path}/${cmd}/gt.scp \
    --pred ${path}/${cmd}/gen.scp \
    --output_file ${path}/${cmd}/test_result \
    --text ${path}/${cmd}/text \
    --io soundfile \
    --use_gpu True
done
