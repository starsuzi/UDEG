import os
import numpy as np
from tqdm import tqdm
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import pickle, torch

topk_file_path = './data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_1.txt'
mc_file_path = './data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_1mc'

print(topk_file_path)
print(mc_file_path)

topk_input_file = open(topk_file_path, 'r')
mc_input_file = open(mc_file_path, 'r')

topk_dataset_test = topk_input_file.readlines()
mc_dataset_test = mc_input_file.readlines()

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

def calc_diversity(dataset_test):
    print('dataset length: '+str(len(dataset_test)))
    divsersity = 0
    for sentences in tqdm(dataset_test):
        
        test_encoding = tokenizer(sentences, truncation=True, padding='longest', return_tensors="pt")
        lst_total_token = test_encoding['input_ids'][0].tolist()
        sentences_total_token_len = len(lst_total_token)
        sentences_unique_len = len(set(lst_total_token))
        divsersity = divsersity + (sentences_unique_len/sentences_total_token_len)
        
    print('diversity: '+str(divsersity))
    norm_divsersity = divsersity/len(dataset_test)
    print('normalized diversity: '+str(norm_divsersity))

print('===topk===')
calc_diversity(topk_dataset_test)
print('====mc====')
calc_diversity(mc_dataset_test)