# Program coding:

class Person(object):
   def __init__(self, name):
      self.name = name
   def getName(self):
      return self.name
   def isEmployee(self):
      return "Is not an Employee"
class Employee(Person):
   def isEmployee(self):
      return "Is an Employee"
emp = Person("Person1") 
print(emp.getName())
print( emp.isEmployee())
emp = Employee("Person2") 
print(emp.getName())
print( emp.isEmployee())

# Output:
# Person1
# Is not an Employee
# Person2
# Is an Employee
