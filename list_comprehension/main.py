import random
import pandas
# n = [4,6,8, 75, 82, 109]
# m = [x*x for x in n]
# even = [num for num in n if num %2 == 0]
# print(m)
# print(even)
# name = "Angel"
# letters = [letter for letter in name]
# print(letters)
#
#
# num_list = [num *2 for num in range(1,7)]
# print(num_list)

# names = ["swati", "priya", "Hrishi"]
# students_scores = {student: random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student, score) in students_scores.items() if score> 33}
# print(passed_students)
# # long_names = [name.upper() for name in names if len(name)> 4 ]
# # print(long_names)
#
# with open("file1.txt") as file1:
#     names1 = file1.readlines()
# with open("file2.txt") as file2:
#     names2 = file2.readlines()
#
#
# common_names = [int(num) for num in names1 if num in names2]
# print(common_names)


# sentence = "My life is an adventure"
# words = [len(words) for words in sentence.split(' ')]
# nwords = {word: len(word) for word in sentence.split()}
# print(words)
# print(nwords)

result = {"student": ["a", "b", "c"], "score": [9,9.5,8]}

student_dataframe = pandas.DataFrame(result)
# print(student_dataframe)
for (index, row) in student_dataframe.iterrows():
    if row.student == "b" :
        print(row.score)
