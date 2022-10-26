class Person:
    def __init__(self, name, age, country):
        
        
        
        self.name = name
        self.age =age
        self.country =country
        

    @property
    def name(self):
        return self.__country 
    
    @name.setter
    def name(self,value):
        if(value not in['Uganda','Kenya','Tanzania','Congo']):
            raise('country not in East Africa')
        self.__country = value
        
    def __str__(self):
        return f'Name is {self.name} and age is {self.age} and country is {self.country}'
    
person1 =Person('John Doe',16,'Uganda')
person1.name = 'Jimmy'
person1.age = 17
person1.country= 'canada'


print (person1)