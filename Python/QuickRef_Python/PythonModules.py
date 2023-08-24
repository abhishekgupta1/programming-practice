# import Modules
import math
print(math.sqrt(16))  # => 4.0

# from a module 
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# import all
from math import *


import math as m
#shorten module
# => True
math.sqrt(16) == m.sqrt(16)

# functions and attibutes
import math
dir(math)