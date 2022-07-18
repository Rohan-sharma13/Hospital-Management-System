def reverse_string(txt):
    if len(txt)%4==0:
        print(txt[::-1])
    else:
        print(txt)
reverse_string(input("Please enter your string:"))