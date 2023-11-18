n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in range(0,n):
  c=a[i]-b[i]
  res.append(c)
print(res)
