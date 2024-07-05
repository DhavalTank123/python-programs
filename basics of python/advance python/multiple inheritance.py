class a:
    def p(self):
        print("class a")

class b:
     def q(self):
         print("class b")

class c(a,b):
    def r(self):
        print("class c")


if __name__ == '__main__':
    obj = c
    obj.p(1)
    obj.q(1)
    obj.r(1)