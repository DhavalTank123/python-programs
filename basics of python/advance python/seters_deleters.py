
class student:

    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln

    def p(self):
        return f"my full name is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "this email is not"
        else:
            return f"my full name is {self.fname} {self.lname} @ yaaho.com"
    @email.setter
    def email(self,string):
        print("setting..")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        print("delete")
        self.fname = None
        self.lname = None


if __name__ == '__main__':
    s = student("dhaval","tank")
    print(s.email)
    s.name = "raj"
    s.email = "a.b@ yaaho.com"
    print(s.email)
    del s.email
    # print(s,email)
    s.email ="dhaval.tank@yaaho.com"
    print(s.email)
