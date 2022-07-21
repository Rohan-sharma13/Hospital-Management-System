list1=[]
a=int(input("Enter Number Element of list:"))
for i in range(0,a):
    print("Enter",i+1,"Element of List:")
    b=int(input())
    list1.append(b)
for j in range(0,len(list1)):
    total=sum(list1)
print("Sum of All Elments of List:",total)