import torch
from torch.nn.utils.rnn import pad_sequence

from transformers import PegasusForConditionalGeneration


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
        self.max_len = 80

    def forward(self, ids, mask):
        outputs = self.model.generate(                
                input_ids=ids,
                attention_mask=mask,
                num_beams=8,
                no_repeat_ngram_size=3,
                min_length=7,
                max_length=self.max_len,
                do_sample=False,
                #top_k=100,
                num_return_sequences=1)

        batch_size, seq_length = outputs.shape        

        outputs = torch.cat((
            outputs,
            torch.zeros(batch_size, self.max_len - seq_length, dtype=int).to(outputs.device)
        ), dim=1)

        return outputs