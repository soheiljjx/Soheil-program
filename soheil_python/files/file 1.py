with open('files/name.txt','r') as f:
    content = f.readlines()
students = []
for line in content:
    student = line.strip().split(",")
    name = student[0]
    grades = student[1:]
    s = 0
    for i in grades:
        s += int(i)
    avg = s / len(grades)
    students.append((name,avg))
with open("files/jadid.txt","w") as g:
    for student in sorted(students,key=lambda x:x[1],reverse=True):
        print(student[0],student[1],sep=",",file=g)