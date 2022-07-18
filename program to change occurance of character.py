a=input("Please Enter your string:")
b=a[0]
a=a.replace(b,'$')
a=b+a[1:]
print(a)