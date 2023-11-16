a=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
first=min(a)
a.remove(first)
secondmin=min(a)
print(secondmin)
