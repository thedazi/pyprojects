#super classing is inheritance of classes
##this can be done with the command super().__init__() after the initializing of the first class
##example

# class Animal():
#   def __init__(self):
#     self.num_eyes = 2
#   def breathe(self):
#     print('In and out')
  
# class Fish(Animal):
#   def __init__(self):
#     super().__init__()
#  #super classes can take a class and twist the command 
#   def breathe(self):
#     super().breathe()
#     print('in and out, but in the moist')
    
#   def swim(self):
#     print('swimmy swimmy')

# in this case, the fish can do everything that the animal can