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

for student in students:
	count = 0;
	for i in range(11):
		if ( student[i+5] != "-1"):
			count+=1
	num_of_exam_taken[count]+= 1

print(num_of_exam_taken)

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '0 môn', '1 môn', '2 môn', '3 môn', '4 môn', '5 môn', '6 môn', '7 môn', '8 môn', '9 môn', '10 môn', '11 môn',  
explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
plt.title('Tỷ lệ số môn học sinh thi')
ax1.pie(num_of_exam_taken, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()