n=int(input())
a=list(map(int,input().split()))
k=int(input())
a=list(set(a))
for i in range(1,k):
    m=min(a)
    a.remove(m)
print(min(a))
