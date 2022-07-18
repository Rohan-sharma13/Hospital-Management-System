def first_three(txt):
    if len(txt)<3:
        print(txt)
    else:
        print(txt[:3])
first_three(input("Enter your string:"))