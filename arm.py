def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        d=temp%10
        sum=sum+d**3
        temp=temp//10
    if sum==n:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    n=int(input())
    if armstrong(n):
        print("Yes")
    else:
        print("No")
