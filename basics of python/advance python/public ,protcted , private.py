class student:

    var1 = 10    # access whole program
    _var2 = 20  # protected var only for derived class
    __var3 = 30


if __name__ == '__main__':

    print(student.var1)
    print(student._var2)
    # print(student.__var3) private var not access in main function only for class
