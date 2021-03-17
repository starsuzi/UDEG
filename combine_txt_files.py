
lst_files = [
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest0_0.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest000_00.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest000_01.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest1_0.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest001_00.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest001_01.txt',
		'/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_rest001_02.txt'
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
	
fr = open('/home/syjeong/DocExpan/Antique-ir/UPSA/result/lexrank_para_total.txt','w')
print(len(full_txt))
fr.write(full_txt)
fr.close()

#print(len(full_txt))

print('done')

# Merge the predictions into a single file.
#cat /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum? > /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum