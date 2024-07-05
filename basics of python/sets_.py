set1 ={
    1,2,3,2,3,2,3,4,5,6,7,67,8
}       # comman number not add
print(set1)
print(type(set1))
print(max(set1))
print(min(set1))

set2 = {
    10,20,30,40,2
}
print(set1.isdisjoint(set2))        #same not => True otherwise False
print(set1.intersection(set2))      #smae element find and print
print(set1.union(set2))             # print in sequnce and no repate

