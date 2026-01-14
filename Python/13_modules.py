            ### MODULES ###

import my_module


my_module.sum(5, 3, 1)
my_module.printValue("Hola Python")

from my_module import sum, printValue

sum(5, 3, 1)
printValue("Hola python")

import math

print(math.pi)
math.pow(2, 3)
print(math.pow(2, 3))

from math import pi as PI_VALUE
print(PI_VALUE)