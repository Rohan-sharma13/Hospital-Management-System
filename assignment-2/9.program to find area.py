def f_area_rectangle(l,b):
    print("Area of Rectangle = ",l,"*",b,"=",l*b)
def f_area_Squre(s):
    print("Area of square = ",s,"*",s,"=",s*s)
def f_area_triangle(L,B):
    print("Area Of Tringle = ",0.5*L*B)
def f_area_circle(r):
    print("Area Of Circle = ",3.14*r*r)
def f_area_parallel(bs,he):
    print("Area of Parallelgram = ",bs*he)
print("Please Select Shape:\n1.Rectangle\n2.Square\n3.Triangle\n4.Circle\n5.Parallelogram")
while True :
    opt =int(input("Enter Your choice('1','2','3','4','5'):"))
    if opt in (1,2,3,4,5):

        if opt==1:
           l=int(input("Enter lenght of triangle:"))
           b=int(input("Enter Breadth of Rectangle:"))
           f_area_rectangle(l,b)
        elif opt==2:
            s=int(input("Enter Side of Square:"))
            f_area_Squre(s)
        elif opt==3:
            L=int(input("Enter height of Triangle:"))
            B=int(input("Enter Base lenght:"))
            f_area_triangle(L,B)
        elif opt==4:
            r=int(input("Enter Radius of Circle:"))
            f_area_circle(r)
        elif opt==5:
            bs=int(input("Enter base Lenght:"))
            he=int(input("Enter height:"))
            f_area_parallel(bs,he)
        next=input("Would you like to do another calculation(yes/no):")
        if next=="no":
            break
    else:
        print("Invalid Option!")