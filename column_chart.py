#read file data
with open("clean_data.csv", encoding= "utf8", mode="r") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]
#remove last student or emtry student
students.pop()

header = header.split(",")
subjects = header[5:]

for i in range(len(students)):
    students[i] = students[i].split(",")

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]
ave = [0,0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	count = 0;
	total = 0;
	for i in range(11):
		if ( student[i+5] != "-1"):
			count+=1
			total += float(student[i + 5])

	num_of_exam_taken[count]+= 1
	ave[count] += total / count

for i in range(len(num_of_exam_taken)):
	if num_of_exam_taken[i] != 0:
		ave[i] = round(ave[i]/num_of_exam_taken[i], 2)

import numpy as np 
import matplotlib.pyplot as plt  
  
   
# creating the dataset 
labels = ['0 môn', '1 môn', '2 môn', '3 môn', '4 môn', '5 môn', '6 môn', '7 môn', '8 môn', '9 môn', '10 môn', '11 môn'] 
   
figure, axis = plt.subplots()
  
axis.set_ylim(1, 10)
# creating the bar plot 
plt.bar(labels, ave, color ='maroon',  
        width = 0.4) 
  
plt.xlabel("Số môn thi") 
plt.ylabel("Điểm") 
plt.title("Điểm trung bình") 
plt.show() 