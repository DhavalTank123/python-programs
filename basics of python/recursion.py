# recursion

""" find the factorial of given number using iterator"""

# def fact(n):
#     """ parameter is n and this function is return the value"""
#     res = 1
#     for i in range(1,n + 1):
#         res = res * i
#
#     return res

""" find the factorial of given number using recursion """

def fact(n):
    """ parameter is n and this function is return the value"""
    if(n==1 or n==0):
        return 1
    else:
        return n * fact(n-1)


# if __name__ == '__main__':
print(fact(4))
