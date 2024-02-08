s={}
n=int(input("Enter no of students:"))
for i in range(n):
    l=[]
    htno=int(input("Enter htno:"))
    sname=input("Enter sname:")
    s1=int(input("Enter s1 marks:"))
    s2=int(input("Enter s2 marks:"))
    s3=int(input("Enter s3 marks:"))
    s4=int(input("Enter s4 marks:"))
    s5=int(input("Enter s5 marks:"))
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    s[htno]=l
hno=int(input("Enter hno:"))
print("Name of the Student:",s[hno][0])
total=s[hno][1]+s[hno][2]+s[hno][3]+s[hno][4]+s[hno][5]
avg=total//3
print("Total:",total)
print("Average:",avg)
if avg>60:
    print("Pass")
else:
    print("Fail")
