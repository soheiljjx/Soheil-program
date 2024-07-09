class student:
    def __init__(self,name,ave,reshte,vahed):
        self.name=name
        self.ave=ave
        self.reshte=reshte
        self.vahed=vahed
    def __str__(self):
        return f"{self.name} is in {self.reshte}."
class st(student):
    pass
st1=st("ali",15,"math",90)
st2=student("ali",15,"math",90)
print(st1)
print(st2)