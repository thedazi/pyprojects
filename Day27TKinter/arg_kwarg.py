# '*arg' (more imprtantly the *) represents the functions ability to accept infinite arguments

# '**kwarg' (**, or key word arguments) represents the functions ability to accept keywords, which convert 
#         the output into a NOTE dictionary
  ### NOTE the * and ** is only used in defining the function and not in the reuse of the argument name

def add(*args):
  return sum(args)

# print(add(4,5,6,7,45,3,2,5,65,2,2,5,5))


def calculate(n, **kw):
  n += kw['add']
  n *= kw['multiply']
  return n

print(calculate(5, add=30, multiply=3))

class bird:
  def __init__(self, **kw) -> None:
    ## .get() is used here so all arguments aren't required
    self.fly = kw.get('fly')
    self.color = kw.get('color')
    self.size = kw.get('size')
    self.food = kw.get('food')
    
my_bird = bird(fly="yes",color="blue",size="10in",food="worms")

print(my_bird.fly)
    
  