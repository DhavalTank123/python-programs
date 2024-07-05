name = "dhaval"

print(name[0])
print(len(name))

# string slicing

print(name[0:5])      # [0:n-1]
print(name[0:])
print(name[:6])
print(name[:])
print(name[0:5:2], "\n")
# negative slising

# print(name[-6:0])  # [n:]
print(name[-6:])
# print(name[:0])
print(name[:])
# print(name[-5:0])

# function in string

print(name.isalnum())      # not space in string then False otherwise True
print(name.count("a"))                      # count the latter in string
print(name.capitalize())                    # upper case for first latter of string
print(name.find("h"))                       # find and return position
print(name.lower())                         # lower case in first charctor of string
print(name.replace("dhaval", "nikhil"))     # replace into nikhil
print(name)