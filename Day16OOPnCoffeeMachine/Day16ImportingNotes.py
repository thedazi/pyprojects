from turtle import Turtle, Screen, right

#classes are constructed to run jobs easily.
##They can can attributes (variables) and profound actions (methods)
### so essentially, the object has attributes that can be called in the form of 'class.attribute'
## In addition to this, attributes are edited with {attribute} = smthing
# Whereas methods are used like {method}(smthing)


#### STEPS IN ORDER TO OPEN A NEW TERMINAL AND DOWNLOAD PACKAGES

#### 1 CTRL + SHIFT + ` to open new terminal
#### 2 to enable scripts in virtual environment, run "Set-ExecutionPolicy RemoteSigned"
## and then run 
# """py -3 -m venv .venv
# .venv\scripts\activate"""
#### 3 type "python -m pip install {package name}" to download
#### 4 run "Set-ExecutionPolicy Restricted" to re-restrict policy 

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")

# timmy.left(90)
# timmy.fd(200)
# timmy.right(90)
# timmy.fd(60)
# timmy.right(90)
# timmy.fd(100)
# timmy.right(90)
# timmy.fd(60)
# timmy.backward(60)
# timmy.left(90)
# timmy.fd(100)
# timmy.left(90)
# timmy.fd(90)
# timmy.left(90)
# timmy.fd(150)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align = "l"
# print(table)