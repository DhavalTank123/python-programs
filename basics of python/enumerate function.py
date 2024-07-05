l = [1, 2, 3, 4, 5, 6]



i = 0
# for i in l:
#     if(i%2==0):
#         print(i)
#     i += 1


for i, item in enumerate(l):
    if (i % 2 == 0):
        print(f"{item}")
