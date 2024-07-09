x= lambda a:a*2
y= lambda a:a*3
b=[5,6,3,8,9,10]
c=list(map(x,b))
d=list(map(y,b))
e=[]
for i in range (0,6):
    z=c[i]*d[i]
    e.append(z)
print(e)

