m=int(input())
count=0
for n in range(1,m+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
        if c>3:
            break
    if c==2:
        print(n,end=' ')
        count=count+1
print()
print(count)
