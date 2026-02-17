from datasets import load_dataset, Audio
import os

HF_TOKEN = os.getenv("HF_TOKEN")

dataset = load_dataset("MeiWu1123/VoiceBank-DEMAND-16k")

dataset = dataset.cast_column("clean", Audio(decode=False))
dataset = dataset.cast_column("noisy", Audio(decode=False))

train_data = dataset["train"]

sample = train_data[0]
print(sample.keys())