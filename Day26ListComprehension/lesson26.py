numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

range_list = [n*2 for n in range(1,5)]
# print(range_list)

names = ['Will','Allie','Ralph','Kat','Lorenzo','Jackson','Carl','Freddie']
long_names = [name.upper() for name in names if len(name) > 5]


import random
import pandas
student_scores = {student:random.randint(1,100) for student in names}


passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}
# print(passed_students)


student_data = {
  "students": ["Allie", "Jakob", "Leo"],
  "score": [56, 76, 90]
}

# for (key, value) in student_data.items():
  # print(key)
  # print(value)
  
student_dict_frame = pandas.DataFrame(student_data)
# print(student_dict_frame)

 #looping through a data frame
# for (key, value) in student_dict_frame.items():
#   print(value)
  
#loop through rows of a data frame
for (index, row) in student_dict_frame.iterrows():
  if row.students == "Allie":
    print(row.students)
    # students/score from original 'student_data' dictionary
    
