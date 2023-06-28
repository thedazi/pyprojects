# file = open('Day24\my_file.txt')
# content = file.read()
# print(content)
# file.close()  

#mode a= append, r=read, w=write (write will delete everything anew each time)
#if the file name is new, then it will make a new one
with open('Day24 (dictionaries/file editing)/made_file', mode='a') as file:
    for x in range(10):
        file.write("\nhopefully this works")
        
    