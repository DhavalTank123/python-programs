# local and global variables
a = 10
# def fun():
#     a = 20
#     print(a)
# fun()
# print(a)

# access global var

def fun():
    global a
    a = 20  # its change in global variable value
    print(a)

fun()

print(a)