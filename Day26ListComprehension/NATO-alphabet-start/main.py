import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_data = pandas.read_csv('Day26ListComprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in phonetic_data.iterrows()}
print(phonetic_dict.keys()) 
# works!

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
  user_input = input("Type the word to be spelled out with NATO phonetics: ").upper()
  try:
    result = [phonetic_dict[letter] for letter in user_input]

  except KeyError:
    print('Sorry, only letters in the alphabet please.')
    generate_phonetic()
  else:
    print(result)
  
generate_phonetic()

