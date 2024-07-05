def fun1():
    l = 20
    def fun2():
        global l
        l = 50
        print(l)
    fun2()

fun1()
