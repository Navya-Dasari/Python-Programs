m=[]
n=int(input())
for i in range(n):
    x=int(input())
    m.append(x)
min=m[0]
max=m[0]
for i in range(n):
    if m[i]>max:
        max=m[i]
    elif m[i]<min:
        min=m[i]
print(max-min)
