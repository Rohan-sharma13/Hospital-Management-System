from ast import Return
from errno import ENAMETOOLONG


class Emp:
    def _init_(self,eid,ename,esal):
        self.eid=eid
        self.enam=ename 
        self.esal=esal 
    def _str_(self):
        return "emp id=%d emp name =%s Emp sal=%g(self.eid,self.ename,self.esal"
class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()
'''Output=
static method 1'''