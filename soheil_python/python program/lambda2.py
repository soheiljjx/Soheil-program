import random2 as r2
a=[]
for x in range (1,101):
    x=r2.randint(1,6)
    a.append(x)
x= lambda a:a*2
y= lambda b:b*3
b=list(map(x,a))
c=list(map(y,a))
z=[]
for x in range (0,100):
    y=c[x]/b[x]
    z.append(y)
print(z)
