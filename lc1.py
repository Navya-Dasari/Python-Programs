def num(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if n==sum:
       return True
    else:
       return False
n=int(input())
l=[i for i in range(1,n+1) if num(i)]
for i in l:
    print(i,end=' ')

        
