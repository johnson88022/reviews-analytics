data = []
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		print(len(data))	#笔数进度次数

print(len(data))	#列印出檔案总笔数

print(data[0])	#留言檔第1项留言

print(data[1])


