# write  a program to find maximum value in given three numbers by user

print("enter n1:", end="")
n1 = int(input())

print("enter n1:", end="")
n2 = int(input())

print("enter n1:", end="")
n3 = int(input())

if (n1>n2 and n1>n3) :
    print(f"maximum is {n1}")
elif (n2>n1 and n2>n3):
    print(f"maximum is {n2}")
else:
    print(f"maximum is {n3}")

