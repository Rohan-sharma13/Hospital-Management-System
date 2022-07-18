a=input("Please enter your string:")
if len(a)<2:
    print("Empty string")
b=a[0:2]+a[-2:]
print(b)