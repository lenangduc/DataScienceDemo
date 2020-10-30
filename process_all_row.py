import csv
file = open("raw_data.txt", "r")

datas = file.read().split("\n")

#write header to csv
with open("clean_data.csv", encoding="utf8", mode="w", newline='') as file_csv:
	header = ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
	writer = csv.writer(file_csv)
	writer.writerow(header)

sbd = 2000000

file = open("sbd_miss.txt", mode="r")
sbd_miss = file.read().split(",")

for data in datas:
	sbd += 1

	if str(sbd) in sbd_miss:
		continue

	sbd_str = "0" + str(sbd)
	data = data.split("\\n")

	for i in range(len(data)):
		data[i] = data[i].replace("\\r", "")
		data[i] = data[i].replace("\\t", "")


	for i in range(len(data)):
		tags = []
		for j in range(len(data[i])):
			if data[i][j] == "<":
				begin = j
			if data[i][j] == ">":
				end = j
				tags.append( data[i][begin: end + 1])
		for tag in tags:	
			data[i] = data[i].replace(tag, "")

	#remove leading whiteSpace.
	for i in range(len(data)):
		data[i] = data[i].strip()

	#remove enpty lines
	unempty_lines = []
	for i in range(len(data)):
		if data[i] != "":
			unempty_lines.append(data[i])
		
	data = unempty_lines

	#chouse relevant information
	name = data[7]
	dob = data[8]
	scores = data[9]

	# load unicode table
	chars = []
	codes = []

	file = open("unicode.txt", encoding="utf8")
	unicode_table = file.read().split("\n")

	for code in unicode_table:
		x = code.split(" ")
		chars.append(x[0])
		codes.append(x[1])

	#replace special characters in name and scores
	for i in range(len(chars)):
		name = name.replace(codes[i], chars[i])
		scores = scores.replace(codes[i], chars[i])

	for i in range(len(name)):
		if name[i:i+2] == "&#":
			name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

	for i in range(len(scores)):
		if scores[i:i+2] == "&#":
			scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]

	# change to lower case
	name = name.lower()
	scores = scores.lower()

	#split dob
	dob_list = dob.split("/")
	dd = int(dob_list[0])
	mm = int(dob_list[1])
	yyyy = int(dob_list[2])

	data = [sbd_str, name.title(), str(dd), str(mm), str(yyyy)]
	#remove :
	scores = scores.replace(":", "")
	scores = scores.replace("khxh ", "khxh   ")
	scores = scores.replace("khtn ", "khtn   ")

	scores_list = scores.split("   ")

	for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
		if subject in scores_list:
			data.append(str(float(scores_list[scores_list.index(subject) + 1])))
		else:
			data.append("-1")
	# write data to csv
	with open("clean_data.csv", "a", encoding="utf-8", newline='') as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)
