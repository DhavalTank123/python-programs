# comprehensions


# lis = []
# for i in range(1,101):
#     if i % 2 == 0:
#         lis.append(i)
#
# if __name__ == '__main__':
#     print(lis)

#list comprehensions

# lis=[i for i in range(1,101) if i % 2 == 0]
# print(lis)
#
# # dictionary comprehensions
#
# dic = {
#     1: "food",
#     2: "food2"
# }
# dic = {i: f"food{i} " for i in range(1,101)}
#
# print(dic)
#
# dic2 ={value: key for key,value in dic.items()}     #reverse dictionary
# print(dic2)

# set

s ={i for i in ["set1","set2"]}
print(s)

gen = ( i for i in range(5))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())