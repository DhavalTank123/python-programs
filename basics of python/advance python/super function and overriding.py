class raju:
    classvar1 = "raju"

    def __init__(self):
        self.classvar1 = "raju1"

class rahul:
    classvar1 = "rahul"

    def __init__(self):
        super().__init__()
        self.classvar1 = "rahul1"

ob1 = raju()
ob2 = rahul()
print(ob1.classvar1)    # overriding for instance variable not claa variable
print(ob2.classvar1)