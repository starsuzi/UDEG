
lst_files = [
		'/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_3mc1',
		'/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_3mc2',
		'/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_3mc3'
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
	
fr = open('/home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_pegasus_xsum_beam8_minlen5_3mc','w')
fr.write(full_txt)
fr.close()

print('done')

# Merge the predictions into a single file.
#cat /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum? > /home/syjeong/DocExpan/Antique-ir/data/text_format/tokenized/test_bart_xsum