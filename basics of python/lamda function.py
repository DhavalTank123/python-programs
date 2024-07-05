# lambda function
# minus = lambda a, b: a-b
# print(minus(8, 4))
#
#

marks2 = [["dhaval", 2],["nikhil", 1]]
print(marks2)
# def srt(a):
#     return a[1]
#
#
#
# marks2.sort(key=srt)
# print(marks2)
marks2.sort(key=lambda a: a[1])
print(marks2)