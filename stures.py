sno=int(input("Enter rollno:"))
sname=input("Enter name:")
s1=int(input("Enter Java marks:"))
s2=int(input("Enter OS marks:"))
s3=int(input("Enter AFM marks:"))
total=s1+s2+s3
avg=total/3
if avg>=90:
    print("O-Grade")
elif avg>=80:
    print("A-Grade")
elif avg>=70:
    print("B-Grade")
elif avg>=60:
    print("C-Grade")
elif avg>=50:
    print("D-Grade")
else:
    print("Pass") 
