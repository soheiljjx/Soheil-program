n = int(input("how many prime do you want? "))
counter = 0
for i in range(1,10000000):
   result = "prime"
   for j in range(2,i):
       if i % j == 0:
           result = "not prime"
           break
   if result == "prime":
       print(i,end=",")
       counter += 1
       if counter >= n:
           break
       