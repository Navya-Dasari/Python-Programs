def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n):
    if prime(i):
        c=c+1
print(c)
