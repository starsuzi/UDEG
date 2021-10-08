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
args = parser.parse_args()

class IRDataset(Dataset):
    def __init__(self, encodings, collection_size):
        self.encodings = encodings
        self.collection_size = collection_size

    def __len__(self):
        return self.collection_size 

    def __getitem__(self, idx):
        text = {key: val[idx].clone().detach() for key, val in self.encodings.items()}
        return text
    
torch_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

#tokenized document path
with open('./data/antique/tokenized/pegasus_test_text_tokenized', 'rb') as file:
    test_encoding = pickle.load(file) 

#len
print(len(test_encoding['input_ids']))
len_input = len(test_encoding['input_ids'])

test_dataset = IRDataset(test_encoding, len_input)

eval_loader = DataLoader(test_dataset, batch_size=45, shuffle=False, num_workers=8)

model = Net()
model = nn.DataParallel(model, device_ids=[0, 1])
model = model.to(torch_device)

if os.path.exists('./data/antique/abs_summary/test_pegasus_xsum_4mc'):
  os.remove('./data/antique/abs_summary/test_pegasus_xsum_4mc')
else:
  print("The file does not exist")

filePath = './data/antique/abs_summary/test_pegasus_xsum_4mc'

for batch in tqdm(eval_loader):
    model.eval()
    matrix_tgt_text = []
    with torch.no_grad():
        for i in range(0,4):
            model.train()

            batch["input_ids"] = batch["input_ids"].to(torch_device)
            batch["attention_mask"] = batch["attention_mask"].to(torch_device)

            translated = model(
                ids=batch["input_ids"],
                mask=batch["attention_mask"],
            )

            tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
            matrix_tgt_text.append(tgt_text)

        arr_tgt_text = np.array(matrix_tgt_text)

        for j in range(0,len(batch['input_ids'])):
            concat_summary = ' '.join(arr_tgt_text[:, j])
            with open(filePath, 'a+') as lf:
                while '\n' in concat_summary:
                    concat_summary = concat_summary.replace("\n", '')
                lf.write(concat_summary)
                lf.write('\n')
            