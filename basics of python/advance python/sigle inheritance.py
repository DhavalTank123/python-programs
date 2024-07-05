class a:
    def p(self):
        print("class a")
class b(a):
     def q(self):
         print("class b")

if __name__ == '__main__':
    obj = b
    obj.p(1)
    obj.q(1)