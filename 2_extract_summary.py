import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import pickle, json
import os, gc
import argparse

gc.collect()
torch.cuda.empty_cache()

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=int, default=1, help='CUDA device')
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

torch_device = torch.device("cuda:"+str(args.device))

model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)

with open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_text_tokenized', 'rb') as file:
    test_encoding = pickle.load(file)

test_encoding = test_encoding.to(torch_device)
#len is 403666
test_dataset = AntiqueDataset(test_encoding, 403666)
eval_loader = DataLoader(test_dataset, batch_size=20, shuffle=False)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

if os.path.exists('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum'):
  os.remove('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum')
else:
  print("The file does not exist")

filePath = '/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum'

for batch in tqdm(eval_loader):
    model.eval()
    with torch.no_grad():
        # translated = model.generate(**batch, min_length=50, num_beams=5)
        translated = model.generate(**batch)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

        with open(filePath, 'a+') as lf:
            lf.write('\n')
            lf.write('\n'.join(tgt_text))

with open(filePath, 'r') as fin:
    data = fin.read().splitlines(True)
with open(filePath, 'w') as fout:
    fout.writelines(data[1:])
