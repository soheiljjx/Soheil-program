n = eval(input("enter a number: "))
s = []
for i in range(1,n):
    if n % i == 0:
        s.append(i)
if sum(s) == n:
    print("perfect")
else:
    print("not perfect")

print(s,sum(s))