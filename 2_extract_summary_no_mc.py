import torch
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
parser.add_argument('--device', type=int, default=1, help='CUDA device')
parser.add_argument('--batch_size', type=int, default=10, help='batch')
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

torch_device = torch.device("cuda:"+str(args.device) if torch.cuda.is_available() else 'cpu')

model_name = 'google/pegasus-cnn_dailymail'
#model_name = 'facebook/bart-large-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
#tokenizer = BartTokenizer.from_pretrained(model_name)

#tokenized document path
with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/pegasus_test_text_cnn_dailymail', 'rb') as file:
    test_encoding = pickle.load(file)
#with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/bart_test_text_tokenized1', 'rb') as file:
#    test_encoding = pickle.load(file)
#with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/temp', 'rb') as file:
#    test_encoding = pickle.load(file)

test_encoding = test_encoding.to(torch_device)
#len is 403666
print(len(test_encoding['input_ids']))
test_dataset = AntiqueDataset(test_encoding,len(test_encoding['input_ids']))
eval_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
#model = BartForConditionalGeneration.from_pretrained(model_name).to(torch_device)

if os.path.exists('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_cnn_dailymail_beam8_minlen5'):
  os.remove('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_cnn_dailymail_beam8_minlen5')
else:
  print("The file does not exist")

filePath = '/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_cnn_dailymail_beam8_minlen5'

for batch in tqdm(eval_loader):
    model.eval()
    matrix_tgt_text = []
    with torch.no_grad():
        #translated = model.generate(**batch)
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
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

    with open(filePath, 'a+') as lf:
        lf.write('\n'.join(tgt_text))
        lf.write('\n')