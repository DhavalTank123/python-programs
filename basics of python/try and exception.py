# try and exception

print("Enter no 1")
no1 = int(input())

print("Enter no 2")
no2 = int(input())

try:
    print(f"divsion is : {no1/no2}")
except Exception as e:
    print("errro:-",e)

print("\nhello world")
