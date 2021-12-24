data = []
count = 1    #设定1个记数器,未开始时为0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))

print("檔案读取为完,目前读取了",len(data),"次了")


# 计算留言平均长度
sum_len = 0    #第0则字数为0
for d in data:
	sum_len = sum_len + len(d)	#快写法: sum_len += len(d)
print("每则留言平均",sum_len/len(data),"字")	#留言总字数/留言则数=每则留言平均字数
