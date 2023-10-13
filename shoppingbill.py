kurti=199
legging=499
longfrock=1999
cname=input("Enter Name")
cphn=input("Enter Phone Number")
kq=int(input("Enter no.of Kurtis"))
lq=int(input("Enter no.of Leggings"))
lfq=int(input("Enter no.of Longfrocks"))
bill=(kurti*kq)+(legging*lq)+(longfrock*lfq)
if bill>=1000:
    dis=bill*15/100
elif bill>=500:
    dis=bill*10/100
elif bill>=300:
    dis=bill*5/100
else:
    dis=bill*3/100
tbill=bill-dis
gst=tbill*12/100
amount=tbill+gst
print("The total bill is:",amount)
print("Thank you")
