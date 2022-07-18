a=input("Please enter Your sentance:")
b= dict()
word=a.split()
for word in word:
        if word in b:
            b[word] += 1
        else:
            b[word] = 1
print(b)