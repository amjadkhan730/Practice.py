
# Python Classes/Objects=-

                # Python is an object oriented programming language.

               # Almost everything in Python is an object, with its properties and methods.

              # A Class is like an object constructor, or a "blueprint" for creating objects.
              
# Class Create=
                #  To create a class, use the keyword class,,
                
        # Examnple=
        
                # Create a class named MyClass, with a property named x:                    
                          
class myclass:
    x=5
print(myclass())  

p1=myclass()
print(p1.x)


#The __init__() Function
                  
                  #The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

                 #To understand the meaning of classes we have to understand the built-in __init__() function.

                #All classes have a function called __init__(), which is always executed when the class is being initiated.

               #Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
      
 # Example=
           
#class person:
 #       def__init__(self, name, age):
  #     self.age=age
#p1=person("Amjad",20)                   
#print(p1.name)
#print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
