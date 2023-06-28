## Constructor
# def __init__(self, attributes):
##   initialise attributes^^
#   self.seats = seats
#   ^^^ this seats up the attributes  

###NEW COMMAND
# CTRL + D on selected variables to select all of the same name variables

class User:
  def __init__(self, user_id, username) -> None:
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
  #in the case of not initializing the followers, all will be set at the base value given

  def follow(self, user):
    user.followers += 1
    self.following += 1
  

user_1 = User("4242", "Zak")
user_2 = User('002', 'Mike')

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)


# user_1.id = "881"
# user_1.username = 'zak'

