from tqdm import tqdm

input_file = open('./data/text_format/tokenized/test_pegasus_xsum_topk_5_sep_0', 'r')

output_file_1 = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_1_0.txt', 'w')
output_file_2 = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_2_0.txt', 'w')
output_file_3 = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_3_0.txt', 'w')
output_file_4 = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_4_0.txt', 'w')
output_file_5 = open('./data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_5_0.txt', 'w')

lst_document = input_file.readlines()

for multi_sentence in tqdm(lst_document):
    
    multi_sentences = multi_sentence.split('[*SEP*]')
    
    output_file_1.write(multi_sentences[0]+'\n')
    output_file_2.write(multi_sentences[0]+' '+multi_sentences[1]+'\n')
    output_file_3.write(multi_sentences[0]+' '+multi_sentences[1]+' '+multi_sentences[2]+'\n')
    output_file_4.write(multi_sentences[0]+' '+multi_sentences[1]+' '+multi_sentences[2]+' '+multi_sentences[3]+'\n')
    output_file_5.write(multi_sentences[0]+' '+multi_sentences[1]+' '+multi_sentences[2]+' '+multi_sentences[3]+' '+multi_sentences[4])
    #print(multi_sentences[4])
    


