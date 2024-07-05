f = open("abcd.txt")
try:
    f = open("bacd.txt")
except Exception as e:
    print(e)
else:
    print("no error")
finally:
    f.close()
    print("terminate")