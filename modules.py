
# Modules=
       
            #  Consider a module to be the same as a code library.

            #A file containing a set of functions you want to include in your application.
            
            # To create a module just save the code you want in a file with the file extension .py
            
            
 # Example    
           # Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)
 
 
 # Now we can use the module we just created, by using the import statement:
 
import modules

modules.greeting("Amjad khan")



person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}



import modules
x = modules=person1["age"]
print(x)

from modules import person1
print(person1["name"])


import calendar
print(calendar.month(2023,2))

