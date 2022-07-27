def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("Zero is not a valid argument here")
     else:
        print("result is", result)
     
a=int(input("Enter Dividend:"))
b=int(input("Enter Divisor:"))
divide(a,b)