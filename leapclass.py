class Year:
    def leap(self,y):
        if(y%400==0 or y%4==0 and y%100!=0):
            return True
        else:
            return False
y=int(input("Enter Year:"))
x=Year()
if x.leap(y):
    print("Leap Year")
else:
    print("Not Leap Year")
