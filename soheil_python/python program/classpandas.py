import pandas as pd
mydata={"phone":["samsung","apple","xiaomi"],
        "laptop":["dell","lenovo","toshiba"],
        "M.B":["asus","Giga","asrock"]}
d=pd.DataFrame(mydata)
df=pd.ExcelWriter("test2.xlsx",engine="xlsxwriter")
d.to_excel(df,"sheet1",index=False)
df.close()