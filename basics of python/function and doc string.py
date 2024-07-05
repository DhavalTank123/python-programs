# built in functions

print(print)
print(sum)
print("sum is: ",sum((10, 20)))    # tupal

#user define function

# doc-string



def avg(a,b,c):
    """this program is  find average of three numbers"""
    return (a+b+c)/3

if __name__ == '__main__':   # main functioon its use for import another program

    print("avg is ", avg(10, 20, 30))
    print(avg.__doc__)
