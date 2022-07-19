num=int(input("Enter the value integer:"))
fact=1
if num<0:
    print("factrial of negative number does not exist!")
elif num==0:
    print("factorial of 0:",fact)
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,":",fact)