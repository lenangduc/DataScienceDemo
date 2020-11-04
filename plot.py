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

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

#look through all students 
for student in students:
    #iterate through  all subject
    for i in range(5, 16):
        if student[i] == "-1":
            not_take_exam[i - 5] += 1

not_take_exam_percentage =  [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0, total_subject):
    not_take_exam_percentage[i] = round( not_take_exam[i] * 100 / total_student, 2)
    

#plot barchart
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

y_pos = np.arange(total_subject)

plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)
plt.xticks(y_pos, subjects)

axis.set_ylim(1, 100)
plt.ylabel('percentage')
plt.title('Số học sinh không thi hoặc không đăng kí')

# Make some labels.
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.show()

