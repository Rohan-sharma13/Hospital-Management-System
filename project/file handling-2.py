f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
f=open("E:\python\demofile2","r")
print(f.read())