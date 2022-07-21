list1=[]
a=int(input("Enter Number Element of list:"))
for i in range(0,a):
    print("Enter",i+1,"Element of List:")
    b=int(input())
    list1.append(b)
total=sum(list1)
avg=total/a
t=list[0]
m=list[0]
for j in range(0,len(list1)):
    if t<=list1[j]:
        t=list[j]
    if m>=list[j]:
        m=list[j]

