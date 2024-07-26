#Super keywords and polymorphism:

###task 1:
##
##class shape():
##    def area(self):
##        return 0
##
##class rectangle(shape):
##    def __init__(self,width,height):
##        self.width=width
##        self.height=height
##
##
##    def area(self):
##        return self.width*self.height
##
##objrectangle=rectangle(13,20)
##print(objrectangle.area())


# ###task 2:
# ##
# class person():
#    def __init__(self,name):
#     self.name=name

# class student(person):
#    def __init__(self,name,grade):
#        super().__init__(name)
#        self.grade=grade

#    def display(self):
#        print("Name:",self.name)
#        print("Grade:",self.grade)

# obj1=student("mukilan","A Grade")
# obj1.display()/


###task 4:
# class Employee():
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary

# class Manager(Employee):
#    def __init__(self, name, salary, department):
#        super().__init__(name, salary)
#        self.department = department



#    def display(self):
#        print("Name:",self.name)
#        print("Salary:",self.salary)
#        print("department:",self.department)

# obj1=Manager("mukilan",10000,"toka")
# obj1.display()


# #task 3:

# class vehicle():
#     def start(self):
#         print("vehicle started")



# class car(vehicle):
#     def start(self):
#         print("car started")


# objcar=car()
# objcar.start()/


#task 5:

# class Animal:
#     def sound(self):
#         print("animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Bird(Animal):
#     def sound(self):
#         print("Birds print")

# Animal=Animal()
# Animal.sound()

# Dog=Dog()
# Dog.sound()

# objbird=Bird()
# objbird.sound()










