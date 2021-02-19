from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from path import Path
from tqdm import tqdm

input_file  = open('./data/text_format/test_text.txt', 'r', encoding='latin1')
#input_file  = open('./marco_temp/marco_temp.txt', 'r')

lst_document = input_file.readlines()
input_file.close()

for doc in tqdm(lst_document):
    #print(doc)
    doc = doc.lower()
    parser = PlaintextParser.from_string(doc, Tokenizer('english'))

    summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    summary = summarizer(parser.document, 1)
    try:
        if len(str(summary[0]).split()) < 2:
            summarised_sentence = str(summary[1]).rstrip()
        else: 
            summarised_sentence = str(summary[0]).rstrip()
    except:
        summarised_sentence = ' '
        #print(doc)
    #print(summarised_sentence)

    output_key = open('./data/text_format/lexrank/lexrank.txt', 'a')
    output_key.write(summarised_sentence)
    output_key.write('\n')
    output_key.close()