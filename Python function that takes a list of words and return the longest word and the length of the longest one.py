l1=[]
n=int(input("Enter No of Elements of List:"))
for i in range(0,n):
    print("Enter Element No.",i+1)
    a=input()
    l1.append(a)
max=len(l1[0])
temp=l1[0]
for j in range(0,n):
    if (len(l1[j])>=max):
        max=len(l1[j])
        temp=l1[j]
print("The word with longest lenght is","'",temp,"'","and its lenght is:",max)