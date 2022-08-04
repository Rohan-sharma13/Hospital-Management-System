from audioop import avg


num=int(input("Enter total no students"))
dic={}
for i in range(0, num):
    name = input("Enter the student's name: ")
    math = int(input("Enter the Math mark: "))
    eng = int(input("Enter the English mark: "))
    ph = int(input("Enter the Science mark: "))
    Av = ((math + eng + ph) / 3)
    dic[name]=Av
print(dic)
