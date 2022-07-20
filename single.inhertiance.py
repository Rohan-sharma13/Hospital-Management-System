class Parent_class(object): 
        
    def __init__(self, value1,value2): 
        self.value1 = value1 
        self.value2 = value2
   
    def Addition(self) : 
        print(" Addition value1 : " , self.value1)
        print(" Addition value2 : " , self.value2)
        return self.value1 + self.value2
        
    def multiplication(self) :
        print(" multiplication value1 : " , self.value1)
        print(" multiplication value2 : " , self.value2)
        return self.value1 * self.value2
        
    def subraction(self) :
        print(" subraction value1 : " , self.value1)
        print(" subraction value2 : " , self.value2)
        return self.value1 - self.value2
class Child_class(Parent_class):    
    pass
      
Object1 = Child_class(10,15)  
print(" Added value :" , Object1.Addition() ) 
print( " " )
Object2 = Child_class(20,30)  
print(" Multiplied value :" , Object2.multiplication() ) 
print( " " )
Object3 = Child_class(50,30) 
print("Subracted value :" , Object3.subraction() ) 