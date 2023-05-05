# import csv
#
# with open("227 - weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#
#     for row in data:
#         temp.append(row[1])
#     temp.remove(temp[0])
#     print(temp)

import pandas
data= pandas.read_csv("227 - weather-data.csv")
# print(data) # type- dataframe
# print(data["temp"]) #type - series
# print(data.temp)
#
# data_list = data.to_dict()
# print(data_list)
# temp_list = data["temp"].to_list()
# print(temp_list)


# sum = 0
# for t in temp_list:
#     sum+= t
# avg_temp = sum / len(temp_list)
# print(avg_temp)

# average = sum(temp_list)/len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].idxmax())

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.condition)
print(monday.temp*9/5 + 32)

marks_list = {"stu":["hrishi", "swati", "others"], "marks": [9, 8, 7]}
new_data= pandas.DataFrame(marks_list)
new_data.to_csv("new_data.csv")
print(new_data)