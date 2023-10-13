year=int(input("Enter year"))
if year%4==0 and year%100!=0:
    print("Given year is Leap Year")
elif year%400==0:
    print("Given Year is Leap Year")
else:
    print("Given Year is not Leap Year")
