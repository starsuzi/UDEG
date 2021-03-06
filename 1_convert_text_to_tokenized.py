import os
import json
import argparse
import numpy as np
from tqdm import tqdm
from transformers import (
    PegasusForConditionalGeneration,
    PegasusTokenizer,
    BartForConditionalGeneration,
    BartTokenizer,
)
import pickle, os, json, torch

input_file = open(
    "/home/syjeong/UDEG/data/antique/test_text.txt",
    "r",
)

dataset_test = input_file.readlines()
print(len(dataset_test))

model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)

test_encoding = tokenizer(
    dataset_test, truncation=True, padding="longest", return_tensors="pt"
)

path = './data/antique/tokenized'
os.makedirs(path, exist_ok=True)

with open(
    "./data/antique/tokenized/pegasus_test_text_tokenized",
    "wb",
) as file:
    pickle.dump(test_encoding, file)

print(len(dataset_test))

print("end")
