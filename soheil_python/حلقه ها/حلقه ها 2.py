number = int(input("enter a number: "))
for n in range(1,number):
    result = True
    for i in range(2,n):
        if n % i == 0:
            result = False
    if result == True:
        print(n,end=",")
