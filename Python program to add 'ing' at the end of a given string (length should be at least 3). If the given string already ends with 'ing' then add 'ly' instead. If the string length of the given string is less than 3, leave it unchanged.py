from ast import If


a= input("please Enter your string:")
if len(a)<3:
    print(a)
if a[-3:]=="ing":
    a+= "ly"
    print(a)
else:
    a+="ing"
    print(a)




