def insert_string_middle(txt,x):
    if len(txt)%2==0:
        middle=int(len(txt)/2)
    else:
        middle=int(len(txt)/2+1)
    print(txt[:middle]+x+txt[middle:])
insert_string_middle(input("Enter your string:"),input("enter your word:"))