import pke
import string
from nltk.corpus import stopwords
import pickle
from tqdm import tqdm
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--in_path',default='./data/text_format/split/test_text.txt04', type=str)
parser.add_argument('--out_path',default='./data/text_format/keyphrase/keyphrase04.txt', type=str)
args = parser.parse_args()                   

#input_file = open('./marco_temp.txt', 'r')
input_file = open(args.in_path, 'r')
lst_document = input_file.read().splitlines()
input_file.close()

if os.path.exists(args.out_path):
  os.remove(args.out_path)
  print('erased')
else:
  print("The file does not exist")


lst_str_key = []

# 2. load the content of the document.
for doc in tqdm(lst_document):
    # 1. create a MultipartiteRank extractor.
    extractor = pke.unsupervised.MultipartiteRank()
    #print(doc)
    extractor.load_document(input=doc)

    # 3. select the longest sequences of nouns and adjectives, that do
    #    not contain punctuation marks or stopwords as candidates.
    pos = {'NOUN', 'PROPN', 'ADJ'}
    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    stoplist += stopwords.words('english')
    extractor.candidate_selection(pos=pos, stoplist=stoplist)

    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    extractor.candidate_weighting(alpha=1.1,
                                threshold=0.74,
                                method='average')

    # 5. get the 10-highest scored candidates as keyphrases
    keyphrases = extractor.get_n_best(n=5)
    #print('===')
    
    str_key = ''
    for keyphrase in keyphrases:
        #print(keyphrase[0])
        str_key = str_key + ' ' +keyphrase[0]
    #print(str_key)
    lst_str_key.append(str_key)
    #print(lst_str_key)
    
    output_key = open(args.out_path, 'a')
    output_key.write(str_key)
    output_key.write('\n')
    output_key.close()
    
    #print(keyphrases)

'''
with open(args.out_path, mode="w") as outfile: 
    for s in lst_str_key:
        outfile.write("%s\n" % s)
'''