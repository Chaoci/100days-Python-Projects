# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

data = pd.read_csv("day26-code/NATO-alphabet-start/nato_phonetic_alphabet.csv")
letter_list = data.letter.to_list()
code = data.code.to_list()

data_dict = {element.letter:element.code for (index,element) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("the words you want to transform:").strip().upper()
input_list = [res for res in user_input]
result = []
for i in input_list:
    if i in letter_list:
        ans = data_dict[i]
        result.append(ans)

print(result)