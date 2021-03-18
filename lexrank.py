from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from path import Path
from tqdm import tqdm

input_file  = open('./data/text_format/test_text.txt', 'r', encoding='latin1')
#input_file  = open('./marco_temp/marco_temp.txt', 'r')

lst_document = input_file.readlines()
input_file.close()

output_key = open('./data/text_format/lexrank/lexrank.txt', 'a')

for doc in tqdm(lst_document):
    #print(doc)
    doc = doc.lower()
    parser = PlaintextParser.from_string(doc, Tokenizer('english'))

    summarizer = LexRankSummarizer()
    #Summarize the document with 1 sentences
    summary = summarizer(parser.document, 1)
    try:
        if len(str(summary[0]).split()) < 2:
            summarised_sentence = str(summary[1]).rstrip()
        else: 
            summarised_sentence = str(summary[0]).rstrip()

        output_key.write(summarised_sentence)
        output_key.write('\n')
    except:
        #print(doc)
        summarised_sentence = doc
        output_key.write(summarised_sentence)
    
    #output_key.close()