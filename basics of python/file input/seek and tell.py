# seek() tell ()

f = open("abcd.txt","r")
print(f.readline())
f.seek(1)    # place pointer in 1 position
print(f.readline())
f.close()



print('\n')



f = open("abcd.txt","r")
print(f.readline())
f.tell()   # place pointer in in last position
print(f.readline())
f.close()


