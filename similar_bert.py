import torch
from torch import nn
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, BartForConditionalGeneration, BartTokenizer
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import pickle, json
import os, gc
import argparse
import numpy as np

gc.collect()
torch.cuda.empty_cache()

#random_seed = 2021
#torch.manual_seed(random_seed)
#np.random.seed(random_seed)

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=int, default=0, help='CUDA device')
parser.add_argument('--batch_size', type=int, default=3, help='batch')
args = parser.parse_args()

class AntiqueDataset(Dataset):
    def __init__(self, encodings, collection_size):
        self.encodings = encodings
        self.collection_size = collection_size

    def __len__(self):
        return self.collection_size

    def __getitem__(self, idx):
        text = {key: val[idx].clone().detach() for key, val in self.encodings.items()}
        return text

class CustomPEGASUSModel(torch.nn.Module):
    def __init__(self):
          super(CustomPEGASUSModel, self).__init__()
          self.tok = PegasusTokenizer.from_pretrained('google/pegasus-xsum')
          self.pegasus = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
          ### New layers:
          self.linear1 = nn.Linear(768, 256)
          self.linear2 = nn.Linear(256, 3) ## 3 is the number of classes in this example

    def forward(self, ids, mask):
          #print(self.pegasus)
          
          sequence_output = self.pegasus(ids, attention_mask=mask)

          # sequence_output has the following shape: (batch_size, sequence_length, 768)
          # linear1_output = self.linear1(sequence_output[:,0,:].view(-1,768)) ## extract the 1st token's embeddings
          # linear2_output = self.linear2(linear2_output)

          return sequence_output


torch_device = torch.device("cuda:"+str(args.device) if torch.cuda.is_available() else 'cpu')

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/temp', 'rb') as file:
    test_encoding = pickle.load(file)

test_encoding = test_encoding.to(torch_device)
print(len(test_encoding['input_ids']))
test_dataset = AntiqueDataset(test_encoding,len(test_encoding['input_ids']))
train_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False)

model = CustomPEGASUSModel().to(torch_device)

if os.path.exists('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/theme_temp'):
  os.remove('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/theme_temp')
else:
  print("The file does not exist")

filePath = '/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/theme_temp'

#print(model)
    
for batch in tqdm(train_loader):
    #print(batch)
    matrix_tgt_text = []
    model.train()
    #print(model(batch["input_ids"], batch["attention_mask"]))
    #print(batch["input_ids"])
    a = model(batch["input_ids"], batch["attention_mask"])
    '''
    translated = model.generate(
        input_ids=batch["input_ids"],
        attention_mask=batch["attention_mask"],
        num_beams=8,
        no_repeat_ngram_size=3,
        min_length=7,
        do_sample=False,
        #top_k=100,
        num_return_sequences=1        
    )
    '''
'''
for batch in tqdm(train_loader):
for batch in tqdm(eval_loader):
    model.eval()
    matrix_tgt_text = []
    with torch.no_grad():
        translated = model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            num_beams=8,
            no_repeat_ngram_size=3,
            min_length=7,
            do_sample=False,
            #top_k=100,
            num_return_sequences=1
        )
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        print(translated)
import pdb; pdb.set_trace()

    with open(filePath, 'a+') as lf:
        lf.write('\n'.join(tgt_text))
        lf.write('\n')
'''