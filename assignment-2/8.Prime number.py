def check_prime_no(a):
    flag=False
    if a>0:
        for i in range(2,a):
            if a%i==0:
                flag=True
                break
        if flag==True:
            print("Number is not Prime Number")
        else:
            print("Number is  prime Number")
    else:
        print("Number is not a prime Number")
a=int(input("Enter your Number:"))
check_prime_no(a)