


class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        
    def __str__(self):
         return f"This is {self.name},{self.age}"
      
    #  instance method
    def start_walking(self):
        print('The student is walking')
        
class student(Person):
    def __init__(self, name,age, access_no, program):
        super().__init__ (name, age)
        self.access_no= access_no
        self. program= program 
        
student1 =student('Jane Doe',16,'a6000','BBA')

student1.start_walking()
print(student1)
# Person1= Person('John',70)


# print(Person1)