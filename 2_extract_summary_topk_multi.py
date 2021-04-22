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
#random_seed = 2021
#torch.manual_seed(random_seed)
#np.random.seed(random_seed)

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type=int, default=6, help='batch')
args = parser.parse_args()

class AntiqueDataset(Dataset):
    def __init__(self, encodings, collection_size):
        self.encodings = encodings
        self.collection_size = collection_size

    def __len__(self):
        return self.collection_size

    def __getitem__(self, idx):
        #text = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        text = {key: val[idx].clone().detach() for key, val in self.encodings.items()}
        return text

torch_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name = 'google/pegasus-xsum'
#model_name = 'facebook/bart-large-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
#tokenizer = BartTokenizer.from_pretrained(model_name)

#tokenized document path
with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/pegasus_test_text_tokenized0', 'rb') as file:
    test_encoding = pickle.load(file)
#with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/bart_test_text_tokenized1', 'rb') as file:
#    test_encoding = pickle.load(file)
#with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/temp', 'rb') as file:
#    test_encoding = pickle.load(file)


#len is 403666
print(len(test_encoding['input_ids']))
len_input = len(test_encoding['input_ids'])

test_dataset = AntiqueDataset(test_encoding,len_input)
eval_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=8)

model = Net()
model = nn.DataParallel(model, device_ids=[0, 1])
model = model.to(torch_device)

if os.path.exists('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_topk_5_0'):
  os.remove('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_topk_5_0')
else:
  print("The file does not exist")

filePath = '/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_topk_5_0'

for batch in tqdm(eval_loader):
    model.eval()
    matrix_tgt_text = []
    with torch.no_grad():
        #translated = model.generate(**batch)
        batch["input_ids"] = batch["input_ids"].to(torch_device)
        batch["attention_mask"] = batch["attention_mask"].to(torch_device)
        '''
        translated = model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            num_beams=8,
            no_repeat_ngram_size=3,
            min_length=7,
            max_length=80,
            do_sample=False,
            #top_k=100,
            num_return_sequences=1
        )
        '''
        translated = model(
                ids=batch["input_ids"],
                mask=batch["attention_mask"],
            )
        #import pdb; pdb.set_trace()
        for i in range(0,5):
            tgt_text = tokenizer.batch_decode(translated[:,i,:], skip_special_tokens=True)
            matrix_tgt_text.append(tgt_text)
        #import pdb; pdb.set_trace()
        #import pdb; pdb.set_trace()
    arr_tgt_text = np.array(matrix_tgt_text)
    #import pdb; pdb.set_trace()
    for j in range(0,len(batch['input_ids'])):
        concat_summary = '[*SEP*]'.join(arr_tgt_text[:, j])
        #import pdb; pdb.set_trace() #if newline 없을때까지 
        with open(filePath, 'a+') as lf:
            while '\n' in concat_summary:
                concat_summary = concat_summary.replace("\n", '')
            lf.write(concat_summary)
            #import pdb; pdb.set_trace()
            lf.write('\n')
        
        