lst_files = [
		'./data/text_format/keyphrase/keyphrase00.txt',
        './data/text_format/keyphrase/keyphrase01.txt',
        './data/text_format/keyphrase/keyphrase02.txt',
        './data/text_format/keyphrase/keyphrase03.txt',
        './data/text_format/keyphrase/keyphrase04.txt'	
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
	print("error")	
	
fr = open('./data/text_format/keyphrase/keyphrase.txt','w')
fr.write(full_txt)
fr.close()

print("done")