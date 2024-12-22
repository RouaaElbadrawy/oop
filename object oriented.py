# Public , Protected , Private 
class Person :
    def __init__(self, name):
        self.name = name 
        
    def get_name(self):
        return self.name

class Employee(Person):
    def __init__(self, name, age):
        Person.__init__(self,name)
        self._age = age 
        
    def get_age(self):
        return self.age
        
class Student(Employee):
    def __init__(self, name, age, grade):
        Employee.__init__(self,name,age)
        self.__grade = grade 
      
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade 
    
p1=Person("Ali")
e1=Employee("Alaa", 26)
s1=Student("Hassan", 17, 94) 

print(p1.get_name())
print(e1.get_name(), e1.get_age())  #'Employee' object has no attribute 'age'
print(s1.get_name(), s1.get_age(), s1.get_grade())
    

    
    
