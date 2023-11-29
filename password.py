st=input('Enter Password:')
u=0
l=0
d=0
s=0
sy='@_$'
n=len(st)
for i in st:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i in sy:
        s=s+1
if u>0 and l>0 and d>0 and s>0 and n>=8:
    print("The Password is Strong")
elif u>0 and l>0 and s>0 and n>=8:
    print("The Password is Medium")
elif u>0 or l>0 and d>0 and n>=8:
    print("The Password is Weak")
elif n<8:
    print("The Password is Invalid")
