def f_add(a,b):
    print(a,"+",b,"=",a+b)
def f_subt(a,b):
    print(a,"-",b,"=",a-b)
def f_multi(a,b):
    print(a,"*",b,"=",a*b)
def f_divide(a,b):
    print(a,"/",b,"=",a/b)
def f_modulas(a,b):
    print(a,"%",b,"=",a%b)
print("Please select your operation:")
print("1.Addition\n2.Subtraction\n3.Multipication\n4.Division\n5.modulus")
while True:
    a =(input("Enter Your choice('1','2','3','4','5'):"))
    if a in ('1','2','3','4','5'):
        x=float(input("Enter your first num:"))
        y=float(input("Enter your second num:"))
        if a=="1":
            f_add(x,y)
        elif a=="2":
            f_subt(x,y)
        elif a=="3":
            f_multi(x,y)
        elif a=="4":
            f_divide(x,y)
        elif a=="5":
            f_modulas(x,y)
        next=input("Would your like do another calculation(yes/no):")
        if next=="no":
            break
    else:
        print("Invalid input")
