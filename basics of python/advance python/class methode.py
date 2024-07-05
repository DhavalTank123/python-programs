# class methode we use cls

# class student:
#     holiday = "20 days"
#     @classmethod
#     def change(cls,n):
#         cls.holiday = f"{n} day"
#
#
# if __name__ == '__main__':
#     s = student()
#     s.change(30)
#     print(s.holiday)

class student:

    # holiday = "20 days"

    def __init__(self,ename,eroll):
        self.name = ename
        self.roll = eroll

    @classmethod
    def n(cls,string):
        return cls(*string.split("-"))


if __name__ == '__main__':
    s = student.n("dhaval - 46")
    print(s.name,s.roll)
