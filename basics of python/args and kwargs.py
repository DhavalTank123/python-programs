
# *args and **kwargs

# def fun(a,b):
#     print(a,b)
#

# fun(10,20,30)         # this code gives error when user gives more arguments


# def fun(*args):
#     for i in args:
#         print(i,end="\t")
#
# marks = [1, 2, 3, 5, 7, 4, 23]
# fun(*marks)

def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

d = {
    "A": "abcd",
    "rool_no ": 46
}

fun(**d)        # string is keyword otherwise error
