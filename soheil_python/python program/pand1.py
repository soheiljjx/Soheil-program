import pandas as pd
n=int(input("Enter number of your data?"))
name=[]
lastname=[]
age=[]
for x in range(1,n+1):
    a=str(input("Enter your first name?"))
    b=str(input("Enter your last name?"))
    c=str(input("Enter your age?"))
    name.append(a)
    lastname.append(b)
    age.append(c)
mydate={"name":name,"last name":lastname,"age":age}
df=pd.DataFrame(mydate)
df1=pd.ExcelWriter("test.xlsx",engine="xlsxwriter")
df.to_excel(df1,"sheet1",index=False)
df1.close()