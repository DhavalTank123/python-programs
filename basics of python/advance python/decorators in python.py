# decorators

def fun(function):
    def fun2():
        print("execution is start")
        function()
        print("terminete program")

    return fun2

@fun        # decorator
def minus():
    print(f"subtraction  is 30")

minus()

