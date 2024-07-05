import time

class a:
    def p(self):
        print("class a")
        time.sleep(15)

class b(a):
     def q(self):
         print("class b")
         time.sleep(10)

class c(a):
    def r(self):
        print("class c")
        time.sleep(5)

class d(b,c):
    def s(self):
        print("class d")



if __name__ == '__main__':
    obj = d
    obj.p(1)
    obj.q(1)
    obj.r(1)
    obj.s(1)