from abc import ABCMeta,abstractmethod

class school(metaclass=ABCMeta):
    @abstractmethod
    def uniform(self):
        return "uniform is formal"

class student(school):

    def uniform(self):
        return "student uniform is formal"

    # def uniform(self):
    #     return "student uniform is formal"


obj = student()     # when class have not uniform function its gives error to the compiler

