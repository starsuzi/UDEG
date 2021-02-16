input_file = open('./data/text_format/qrels_test_non-offensive_text.txt', 'r')
lst_qrels = input_file.readlines()

with open('./data/text_format/qrels_test_non-offensive_text_0_3.txt', 'w') as outfile:
    for qrel in lst_qrels:
        e1, e2, e3, qrel_label = qrel.rstrip().split('\t')
        #print(qrel)
        #print(type(qrel_label))
        outfile.write("{0}\t{1}\t{2}\t{3}\n".format(e1,e2,e3,str(int(qrel_label)-1)))


input_file = open('./data/text_format/qrels_test_text.txt', 'r')
lst_qrels = input_file.readlines()

with open('./data/text_format/qrels_test_text_0_3.txt', 'w') as outfile:
    for qrel in lst_qrels:
        e1, e2, e3, qrel_label = qrel.rstrip().split('\t')
        #print(qrel)
        #print(type(qrel_label))
        outfile.write("{0}\t{1}\t{2}\t{3}\n".format(e1,e2,e3,str(int(qrel_label)-1)))
