class Solution:
    def armstrong(self,n):
        temp=n
        sum=0
        while temp>0:
            d=temp%10
            sum+=d**3
            temp//=10
        if sum==n:
            return True
        return False
t=int(input())
for i in range(t):
    n=int(input())
    ob=Solution()
    if ob.armstrong(n):
        print("Yes")
    else:
        print("No")
