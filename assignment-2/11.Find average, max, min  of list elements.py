list1=[]
a=int(input("Enter Number of Elements of list:"))
for i in range(0,a):
    print("Enter",i+1,"Element of List:")
    b=int(input())
    list1.append(b)
total=sum(list1)
avg=total/a
print("Average of Elements of list:",avg)
print("The Smallest Element in this List is : ", min(list1))
print("The Largest Element in this List is : ", max(list1))
