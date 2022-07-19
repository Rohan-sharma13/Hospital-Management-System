a = 10
def f():
 	print ('Inside f() : ', a)
def g(): 
 	a = 20
print('Inside g() : ',a)
def h(): 
 	global a
a = 30
print ('Inside h() : ',a)
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)
'''Output=
Inside g() :  10
Inside h() :  30
global :  30
Inside f() :  30
global :  30
global :  30
global :  30'''