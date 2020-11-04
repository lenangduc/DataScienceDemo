#read file data
with open("clean_data.csv", encoding= "utf8", mode="r") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]
#remove last student or emtry student
students.pop()

total_student = len(students)

#splip header
header = header.split(",")
subjects = header[5:]
total_subject = len(subjects)

#splip each student in list
for i in range(total_student):
    students[i] = students[i].split(",")

#get number of student per age group
#17, 18, ... ,>= 27
num_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
ave_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
for student in students:
	age = 2020 - int(student[4])
	if age >= 27: 
		age = 27
	num_of_student_per_age_group[age - 17] += 1

	count = 0;
	total = 0;
	for i in range(11):
		if ( student[i+5] != "-1"):
			count+=1
			total += float(student[i + 5])

	ave_of_student_per_age_group[age - 17] += total / count

for i in range(len(num_of_student_per_age_group)):
	if num_of_student_per_age_group[i] != 0:
		ave_of_student_per_age_group[i] = ave_of_student_per_age_group[i]/num_of_student_per_age_group[i]
for i in range(len(ave_of_student_per_age_group)):
	ave_of_student_per_age_group[i] = ave_of_student_per_age_group[i] * 7000
print(ave_of_student_per_age_group)
label_age = ['17','18','19','20','21','22','23','24','25','26','>= 27']

#plot barchart
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()
x = np.arange(len(ave_of_student_per_age_group))

plt.bar(x, num_of_student_per_age_group, align='center', alpha=0.5)
plt.plot(x, ave_of_student_per_age_group, color = 'red', marker = 'o')

plt.xticks(x, label_age)

axis.set_ylim(1, 74444)
plt.ylabel('Số lượng')
plt.xlabel('Tuổi')
plt.title('Số học sinh cùng tuổi')

axis2 = axis.twinx()
axis2.set_ylim(1, 10)
axis2.set_ylabel('Điểm trung bình')
axis2.tick_params('y', colors = 'r')

# Make some labels.
rects = axis.patches
for rect, label in zip(rects, num_of_student_per_age_group):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.show()