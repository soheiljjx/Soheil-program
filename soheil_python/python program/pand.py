import pandas as pd
mydata={"cars":["BMW","Ford","Hyndai","Kia"],"models":[2023,2022,2020,2018]}
d=pd.DataFrame(mydata)
df=pd.ExcelWriter("test1.xlsx",engine="xlsxwriter")
d.to_excel(df,"Sheet1",index=False)
df.close()