a=input("Please Enter Your string:")
b=int(input("Enter index (starting from 0) which you want to delete:"))
c=a[:b]+a[b+1:]
print("updated string is:",c)