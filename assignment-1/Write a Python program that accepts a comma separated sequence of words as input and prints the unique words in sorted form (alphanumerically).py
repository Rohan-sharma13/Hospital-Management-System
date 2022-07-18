a=input("Input comma separated sequence of words:")
b=a.split(",")
items=[ i for i in b]
items.sort()
print(items)
print(",".join(items))