def upper_string(txt):
    num=0
    for i in txt[:4]:
        if i.upper()==i:
            num += 1
    if num>=2:
        print(txt.upper())
    else:
        print(txt)
upper_string(input("Enter Your string:"))
