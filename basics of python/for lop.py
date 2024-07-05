# for loop

marks = [10,20,44,32,1,3]
for i in marks:
    print(i,end="\t")


# 2d list

marks2 = [["dhaval",1],["nikhil",2]]
for name ,level in marks2:
    print("\n", name,level,end="\t")


d = dict(marks2)
# print("\n",d)
for item, var in d.items():
    print("\n", item, "there levels is", var)