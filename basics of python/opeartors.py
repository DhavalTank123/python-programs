# """
#     1 Arithmatic operators :-
#         +,-,*,/,%,**
#     2 Assighnment operators :-
#         +=,-=,*=,/=
#     3 Comperision operators :-
#         ==,<=,>=,<,>
#     4 Logical operators :-
#         and,or,not
#     5 Identy operators :-
#         is,is not
#     6 Mebership operators :-
#         in,not in
#     7 Bitwise operators :-
#         &,|,>>,<<
#     8 short hand operators :-
#         print(a>b) if(a>b)else print(b>a)
# """
# #1
#
# print("Enter no 1")
# no1 = int(input())
#
# print("Enter no 2")
# no2 = int(input())
#
# print("add", no1 + no2)
# print("sub", no1 - no2)
# print("muty", no1 * no2)
# print("division", no1 / no2)
# print("modulo", no1 % no2)
# print("power", no1 ** no2) # power find
#
# #2
#
# marks = [10, 20, 44, 32, 1, 3]
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i += 1
#
# #3 and 4
#
# print("enter n1:", end="")
# n1 = int(input())
#
# print("enter n1:", end="")
# n2 = int(input())
#
# print("enter n1:", end="")
# n3 = int(input())
#
# if (n1 > n2 and n1 > n3) :
#     print(f"maximum is {n1}")
# elif (n2 > n1 and n2 > n3):
#     print(f"maximum is {n2}")
# else:
#     print(f"maximum is {n3}")
# #5
# n1=20
# n2=30
#
# if n1 is n2:
#     print("equel")
# else:
#     print("not eual")
#
#
#
# #6
#
# marks2 = [["dhaval",1],["nikhil",2]]
# for name ,level in marks2:
#     print("\n", name,level,end="\t")
#
# # 7
#
# print(1 & 10)
#
#
# # 8
# a = 10
# b = 20
# print("a is max", a>b) if(a > b)else print("b is max", b > a)