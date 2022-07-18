a=input("Please Enter your string:")
b=a.find("not")
c=a.find("poor")
if b<c:
    a=a.replace(a[b:(c+4)],"good")
    print(a)