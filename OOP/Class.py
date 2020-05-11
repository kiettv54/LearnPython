class Person:
    def __init__(self, name, age, male):
        print("Class person được khởi tạo!")
        self.name, self.age, self.male = name, age, male
    
    def getName(self):
        print("Name: %s" %(self.name))
    
    def getAge(self):
        print("Age: %d" %(self.age))
    
    def getMale(self):
        print("Male: %d" %(self.male))
    
    def __del__(self):
        print('Class Person được hủy')
        del self.name,self.age,self.male

person = Person('Vu Thanh Tai', 22, True)
person.getName()
person.getAge()
person.getMale()