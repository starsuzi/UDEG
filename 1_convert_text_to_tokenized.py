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
    "/home/syjeong/DocExpan/Antique-ir/data/text_format/split/split_2/test_text.txt00",
    "r",
)
# input_file = open('/home/syjeong/DocExpan/Antique-ir/data/text_format/temp.txt', 'r')
# input_file = open('/home/syjeong/DocExpan/Antique-ir/data/text_format/split/split_2/test_text.txt00', 'r')

dataset_test = input_file.readlines()
print(len(dataset_test))

model_name = "google/pegasus-xsum"
# model_name = 'google/pegasus-cnn_dailymail'
# model_name = 'facebook/bart-large-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

test_encoding = tokenizer(
    dataset_test, truncation=True, padding="longest", return_tensors="pt"
)

with open(
    "/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/pegasus_test_text_tokenized0",
    "wb",
) as file:
    pickle.dump(test_encoding, file)

print(len(dataset_test))

print("end")
