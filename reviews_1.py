data = []
count = 1    #设定1个记数器,未开始时为0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print("檔案读取为完,目前读取了",len(data),"次了")
