def check_leapyear(a):
    if (((a%4==0)&(a%100!=0))|((a%100==0)&(a%400==0))):
        print("It is leap year")
    else:
        print("Year is not a Leap Year")
a=int(input("Enter Year:"))
check_leapyear(a)