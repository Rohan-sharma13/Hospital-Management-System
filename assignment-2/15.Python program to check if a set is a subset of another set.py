l1,l2,l3=[],[],[]
a=int(input("Enter No elements of 1st set:"))
b=int(input("Enter No elements of 2nt set:"))
c=int(input("Enter No elements of 3rd set:"))
for i in range(0,a):
    print("Element No",i+1,"of set-1:")
    x=input()
    l1.append(x)
for i in range(0,b):
    print("Element No",i+1,"of set-2:")
    y=input()
    l2.append(y)
for i in range(0,c):
    print("Element No",i+1,"of set-3:")
    z=input()
    l3.append(z)
set1=set(l1)
set2=set(l2)
set3=set(l3)
print("Set-1:",set1)
print("Set-2:",set2)
print("Set-3:",set3)
'''while True:
    if set1.issubset(set2):
        print("set-1 is subset of set-2")
    elif set2.issubset(set1)==True:
        print("set-2 is subset of set-1")
    elif set1.issubset(set3)==True:
        print("set-1 is subset of set-3")
    elif set3.issubset(set1)==True:
        print("set-3 is subset of set-1")
    elif set2.issubset(set3)==True:
        print("set-2 is subset of set-3")
    elif set3.issubset(set2)==True:
       print("set-3 is subset of set-2")
       break'''
print("Is set-2 a subset of set-1?: ", set2.issubset(set1))
print("Is set-1 a subset of set-2?: ", set1.issubset(set2))
print("Is set-3 a subset of set-1?: ", set3.issubset(set1))