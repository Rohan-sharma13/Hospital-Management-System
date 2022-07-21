list1=[]
a=int(input("Enter Number Element of list:"))
for i in range(0,a):
    print("Enter",i+1,"Element of List:")
    b=input()
    list1.append(b)
x=list1.copy()
list1.reverse()
print("Your List:",x)
print("Reversed List:",list1)