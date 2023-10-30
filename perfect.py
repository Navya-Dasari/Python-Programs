def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    n=int(input())
    if perfect(n):
        print("Perfect Number")
    else:
        print("Not Perfect Number")
