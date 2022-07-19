num=int((input("Please Enter Your Number:")))
l=len(str(num))
temp=num
add_sum=0
while num!=0:
    a=num%10
    add_sum+=pow(a,l)
    num//10
if add_sum==temp:
    print("Your Number is Armstrong Number")
else:
    print("Number is not Armstrong Number")