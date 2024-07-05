class student:
    def __init__(self, eage):
        self.age = int(eage)

# dunder methode for add
    def __add__(self, other):
        return self.age + other.age

    def __repr__(self):
        return self.age

    def __str__(self):
        return self.age

if __name__ == '__main__':

    obj1 = student("21")
    obj2 = student("32")
    # obj1 = student(10)
    # obj2 = student(20)
    print(obj1 + obj2)  # error
