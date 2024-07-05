# map

n = ['2', '4', '5']

""" using loop """
# for i in range(len(n)):
#     n[i] = int(n[i])
# n[2] = n[2]+1
# print(n[2])

"""using map"""

# num = list(map(int,n))
# print(num)

# def sq(n):
#     return n*n
#
# num = list(map(int,n))
# num = list(map(sq, num))
# print(num)

# num = list(map(int,n))
# num = list(map(lambda x:x*x,num))
# print(num)

# filter


# def f(x):
#     return (x%2==0)
#
# n1 = [2,3,4,5,6,7]
# num = list(filter(f,n1))
# print(num)


# raduce

from functools import reduce

n1 = [1,2,3,4,5]

res = int(reduce(lambda x,y: x*y,n1))
print(res)
