

#Python JSON

         #JSON is a syntax for storing and exchanging data.

         #JSON is text, written with JavaScript object notation.
         
        #Python has a built-in package called json, which can be used to work with JSON data.

#Example

#Import the json module:

import json

   #Parse JSON - Convert from JSON to Python
               
               #If you have a JSON string, you can parse it by using the json.loads() method.

               #The result will be a Python dictionary.
               
               
               
     ##### json support mainly  data type
     
         
 # 1) String ,, 2) number ,, 3) boolean ,, 4) null ,, 5) object ,, 6) array ,,
               
               
                             
#Example

      #Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"Amjad khan", "age":22, "city":"Pakistan"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])       
               
               
               
       #####Convert from Python to JSON
                      
                      #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.        
               
               
    #Example
                           #Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
