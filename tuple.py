num=()
l=list(num)
num=int(input("Enter no of elements of tuple:"))
for x in range(0,num):
    print("Enter Element no.",x+1)
    a=input()
    l.append(a)
b=tuple(l)    
print(b)