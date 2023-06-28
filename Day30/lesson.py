###---------------- Types of Errors

#FileNotFound
# with open("nonexistent_file.txt") as file:
#   file.read()
  
# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non-existent key']

# IndexError
# friut_list = ['fruit1', 'fruit2', 'fruit3']
# fruit = friut_list[3]

# TypeError
# text= 'abc'
# print(text + 5)

###------------------- Exceptions
# try:
#   file = open('a_file.txt')
#   a_dictionary = {'key': 'value'}
#   value = a_dictionary['non-existent key']
#   ## just bare except errors are too broad because they will execute even if it is for a different type of error
#   ##        therefore it is recommended to clarify the excepts with the type of error that could be called from it
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# except KeyError as error_message:
#   print(f'That key {error_message} does not exist')
# else:
#   content = file.read()
#   print(content)
# finally:
#   ###--------------------- Raising my own exception
#   raise TypeError("This is an error that I made up. LOL")

# height = float(input('Input your height: '))
# weight = float(input('Input your weight: '))

# if height > 3:
#   raise ValueError('Human height should not be over 3 meters')

# bmi = weight/height ** 2
# print(bmi)