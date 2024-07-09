class Bank:
    def __init__(self,code,name,lname,fname,acc):
        self.code=code
        self.name=name
        self.lname=lname
        self.fname=fname
        self.acc=acc
    def __str__(self):
        return f"The {self.name} {self.lname} of {self.fname} have {self.code} is {self.acc}."
a1=Bank(124,"ali","reza","hassan",5000)
print(a1)
    