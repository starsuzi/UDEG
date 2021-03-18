import torch
import torch.nn as nn
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from model import Net
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import pickle, json
import os, gc
import argparse
import numpy as np

gc.collect()
torch.cuda.empty_cache()

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"


parser = argparse.ArgumentParser()
#parser.add_argument('--device', type=int, default=0, help='CUDA device')
args = parser.parse_args()

class MSDataset(Dataset):
    def __init__(self, encodings, collection_size):
        self.encodings = encodings
        self.collection_size = collection_size

    def __len__(self):
        return self.collection_size #total: 8841823

    def __getitem__(self, idx):
        #text = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        text = {key: val[idx].clone().detach() for key, val in self.encodings.items()}
        return text
    
#torch_device = torch.device("cuda:"+str(args.device))
torch_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

#tokenized document path
with open('./data/text_format/tokenized/pegasus_test_text_tokenized0', 'rb') as file:
    test_encoding = pickle.load(file) 

"""
test_encoding = {
    'input_ids': test_encoding['input_ids'][start_index : end_index],
    'attention_mask': test_encoding['attention_mask'][start_index : end_index]
}
"""

#len
print(len(test_encoding['input_ids']))
len_input = len(test_encoding['input_ids'])

'''
if torch.cuda.device_count() > 1:
    test_encoding = torch.nn.DataParallel(test_encoding)
'''

# test_encoding = test_encoding.to(torch_device)
test_dataset = MSDataset(test_encoding, len_input)

#import pdb; pdb.set_trace()



eval_loader = DataLoader(test_dataset, batch_size=10, shuffle=False, num_workers=8)
# model = PegasusForConditionalGeneration.from_pretrained(model_name)
# model = nn.DataParallel(model, device_ids=[0, 1])
# model = model.to(torch_device)

model = Net()
model = nn.DataParallel(model, device_ids=[0, 1])
model = model.to(torch_device)

# else:
    # model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

if os.path.exists('./data/text_format/tokenized/test_pegasus_xsum_topk_4mc0'):
  os.remove('./data/text_format/tokenized/test_pegasus_xsum_topk_4mc0')
else:
  print("The file does not exist")

filePath = './data/text_format/tokenized/test_pegasus_xsum_topk_4mc0'

for batch in tqdm(eval_loader):
    model.eval()
    matrix_tgt_text = []
    with torch.no_grad():
        for i in range(0,4):
            model.train()

            batch["input_ids"] = batch["input_ids"].to(torch_device)
            batch["attention_mask"] = batch["attention_mask"].to(torch_device)

            # translated = model(
            #     input_ids=batch["input_ids"],
            #     attention_mask=batch["attention_mask"],
            #     num_beams=8,
            #     no_repeat_ngram_size=3,
            #     min_length=7,
            #     do_sample=False,
            #     #top_k=100,
            #     num_return_sequences=1
            # )

            translated = model(
                ids=batch["input_ids"],
                mask=batch["attention_mask"],
            )

            tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
            matrix_tgt_text.append(tgt_text)

        arr_tgt_text = np.array(matrix_tgt_text)

        for j in range(0,len(batch['input_ids'])):
            concat_summary = ' '.join(arr_tgt_text[:, j])
            #import pdb; pdb.set_trace()
            with open(filePath, 'a+') as lf:
                lf.write(concat_summary)
                lf.write('\n')
            