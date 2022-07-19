number =int(input("Please Enter your number "))
m = len(str(number))
temp = number
add_sum = 0
while temp!=0:
    k = temp%10 
    add_sum +=pow(k,m) 
    temp = temp//10 
if add_sum==number:
    print('Armstrong Number in Python')
else:
    print('Not a Armstrong Number in Python')