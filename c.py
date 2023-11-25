n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(0,n):
    s=0
    for j in range(0,n):
        s+=a[j][i]
    print(s,end=' ')
