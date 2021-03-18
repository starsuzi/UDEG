import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import pickle, json
import os, gc
import argparse

print("GOGO")
gc.collect()
torch.cuda.empty_cache()

parser = argparse.ArgumentParser()
parser.add_argument("--device", type=int, default=0, help="CUDA device")
args = parser.parse_args()


class AntiqueDataset(Dataset):
    def __init__(self, encodings, collection_size):
        self.encodings = encodings
        self.collection_size = collection_size

    def __len__(self):
        return self.collection_size

    def __getitem__(self, idx):
        # text = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        text = {
            key: val[idx].clone().detach()
            for key, val in self.encodings.items()
        }
        return text


torch_device = torch.device("cuda:" + str(args.device))

model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)

# tokenized document path
with open(
    "./tokenized/test_text_tokenized",
    "rb",
) as file:
    test_encoding = pickle.load(file)

test_encoding = test_encoding.to(torch_device)
# len is 403666
print(len(test_encoding["input_ids"]))
test_dataset = AntiqueDataset(test_encoding, len(test_encoding["input_ids"]))
eval_loader = DataLoader(test_dataset, batch_size=20, shuffle=False)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(
    torch_device
)

os.makedirs("decoded", exist_ok=True)
filePath = "decoded/test_pegasus_xsum_k100_minlen5"  # test_pegasus_xsum_beam8_minlen3"

for batch in tqdm(eval_loader):
    model.eval()
    with torch.no_grad():
        translated = model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            # num_beams=8,
            no_repeat_ngram_size=3,
            min_length=7,
            do_sample=True,
            top_k=100,
            # num_return_sequences=3,
        )
        tgt_text = tokenizer.batch_decode(
            translated, skip_special_tokens=True
        )
        # assert len(tgt_text) == 18
        # tmp_tgt_text = []
        # for a in range(6):
        #     b = "|||||".join(tgt_text[3 * a : 3 * (a + 1)])
        #     tmp_tgt_text.append(b)
        # tgt_text = tmp_tgt_text[:]
        # assert len(tgt_text) == 6
        with open(filePath, "a+") as lf:
            lf.write("\n")
            lf.write("\n".join(tgt_text))


with open(filePath, "r") as fin:
    data = fin.read().splitlines(True)
with open(filePath, "w") as fout:
    fout.writelines(data[1:])
