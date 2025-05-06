
class Employee:
    #data members
    __empname=None
    __id=None
    __dept=None
   
 
    def display(self):
        print(f"emp id ={self.__id} , emp name={self.__empname}, dept={self.__dept}")
        
    def __init__(self,id,empname,dept):
        if id>0:
            self.__id=id
        self.__empname=empname
        self.__dept=dept
        self.__company="Test"
    def salarycal():
        pass
        # bs+hra+da-pf
        
   


#working with methods
# using object
emp1=Employee(1,"Rohan","HR")
emp2=Employee(2, "Suraj", "Sales")


emp1.display()
emp2.display()








