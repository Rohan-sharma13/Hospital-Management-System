num=int(input("please enter your integer(postive integer):"))
a1=0
a2=1
count=0
if (num<=0):
    print("Invalid Number!")
elif num==1:
    print("fibonacci series:",a1)
else:
    print("Fibonacci series of ",num,":")
    while count<num:
        print(a1)
        nth= a1+a2
        a1=a2
        a2=nth
        count+=1