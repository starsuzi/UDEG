
lst_files = [
		'/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_5_0.txt',
		'/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_5_1.txt'
		]


full_txt = ""

try :
	for i in range(len(lst_files)):
		
		file_name = lst_files[i]
		print(file_name)
		file_read = open(file_name, 'r')

		full_txt = full_txt + file_read.read()
		
		file_read.close()

except :
	print('error')	
	
fr = open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/topk_splitted/test_pegasus_xsum_topk_5.txt','w')
#print(len(full_txt))
fr.write(full_txt)
fr.close()

#print(len(full_txt))

print('done')

# Merge the predictions into a single file.
#cat /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum? > /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum