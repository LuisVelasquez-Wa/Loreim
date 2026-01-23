            ### TUPLES ###

my_tuple = tuple()
My_other_tuple = ()

my_tuple = (30, 1.65, "Luis", "Velasquez")
My_other_tuple = (35, 60, 30 )
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[6]) IndexError por estar fuera de rango.

print(my_tuple.count(30))
print(my_tuple.index("Velasquez"))
print(my_tuple.index("Luis"))

#my_tuple[1] = 1.80 #TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + My_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[5:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Loreim"
my_tuple.insert(1, "Verde" )
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] #TypeError: 'tuple' object doesn't support item deletion
#del my_tuple #print(my_tuple) NameError: name 'my_tuple' is not defined
