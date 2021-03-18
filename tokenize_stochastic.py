import os
import numpy as np
from tqdm import tqdm
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import pickle, torch

#input_file = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_4.txt', 'r')
input_file = open('./data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_4mc', 'r')


dataset_test = input_file.readlines()[:2]
print('dataset length: '+str(len(dataset_test)))

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

divsersity = 0
for sentences in tqdm(dataset_test):
    #print(sentences)
    '''
    test_encoding = tokenizer(sentences, truncation=True, padding='longest', return_tensors="pt")
    print(test_encoding)
    lst_total_token = test_encoding['input_ids'][0].tolist()
    sentences_total_token_len = len(lst_total_token)
    sentences_unique_len = len(set(lst_total_token))
    divsersity = divsersity + (sentences_unique_len/sentences_total_token_len)
    '''
    test_encoding = tokenizer(sentences, truncation=True, padding='longest', return_tensors="pt")
    #print(test_encoding)
    lst_total_token = test_encoding['input_ids'][0].tolist()
    sentences_total_token_len = len(lst_total_token)
    sentences_unique_len = len(set(lst_total_token))
    divsersity = divsersity + (sentences_unique_len/sentences_total_token_len)
    
print('diversity: '+str(divsersity))
norm_divsersity = divsersity/len(dataset_test)
print('normalized diversity: '+str(norm_divsersity))