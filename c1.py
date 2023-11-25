n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(0,n):
    max=a[0][i]
    for j in range(0,n):
        if a[j][i]>max:
            max=a[i][j]
    print(max,end=' ')
