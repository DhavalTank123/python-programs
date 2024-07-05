marks = [10,20,44,32,1,3]
print(marks)
print(type(marks))

# shorting in list
marks.sort()
print(marks)
marks.reverse()
print(marks)

# slicing in list

print(marks[0])

print(marks[0:None])
print(marks[:])
print(marks[:6])  # n-1

print(marks[-6])
print(marks[::2])
marks.append(55)
marks.insert(6,66)

print(marks)

marks.remove(1)
marks.pop()
print(marks)

# list is change so it is mutable => can change
