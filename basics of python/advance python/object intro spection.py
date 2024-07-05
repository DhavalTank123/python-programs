import seters_deleters
import inspect

print(id(seters_deleters.student)) # adress of object
print(dir(seters_deleters.student)) # dirtory of class

print(inspect.getmembers(seters_deleters.student)) # access mebers of class