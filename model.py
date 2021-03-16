import torch
from torch.nn.utils.rnn import pad_sequence

from transformers import PegasusForConditionalGeneration


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
        #self.model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-cnn_dailymail')
        self.max_len = 80
        self.num_seq = 5

    def forward(self, ids, mask):
        '''
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
        '''
        outputs = self.model.generate(                
                input_ids=ids,
                attention_mask=mask,
                num_beams=8,
                no_repeat_ngram_size=3,
                min_length=7,
                max_length=self.max_len,
                do_sample=True,
                top_k=100,
                num_return_sequences=self.num_seq)
        
        #import pdb; pdb.set_trace()
        batch_size = len(ids)
        outputs = outputs.view(batch_size, self.num_seq, -1)
        batch_size, num_sequence, seq_length = outputs.shape   #batch, num_seq, seq_length     
        temp=outputs
        
        outputs = torch.cat((
            outputs,
            torch.zeros(batch_size,self.num_seq, self.max_len - seq_length, dtype=int).to(outputs.device)
        ), dim=2)
        #import pdb; pdb.set_trace()
        
        return outputs