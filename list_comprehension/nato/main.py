student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_letters = {row.letter: row.code for (index, row) in nato.iterrows() }
# print(dict_letters)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
say = input(" say a word").upper()
# dict_2 = {row.letter: row.code for (index, row) in nato.iterrows() if row.letter.lower() in say}
# dict_3 = {letter: word for (letter, word) in dict_letters.items() if letter.lower() in say}
# print(dict_3)
w_list = [dict_letters[letter] for letter in say]
print(w_list)

