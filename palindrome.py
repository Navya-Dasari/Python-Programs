n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("The Number is not a palindrome")
