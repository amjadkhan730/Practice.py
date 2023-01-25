# variable in Python=-
                
                # variable are container for storing data value,,
                
    # Example=-

#x = 5
#y = "amjad"
#print(x)
#print(y)
#print(type(x))

#x,y,z = 2,3,4
#print(x,y,z)
#x,y,z = "amjad","khan","khattak"
#print(x,y,z)
#x=y=z = "amjad"
#print(x)
#print(y)
#print(z)
#amjad = [1,2,3,4,5,6,7,8]
#x=amjad
#print(x)
         
            #___________***_________#
            
 # Casting=-
             # if u want to specify the data type of variable,this can be done casting,
             
   #Example=-
               
#x = str(5) # x will be '5'                    
#print(x)

#y = int(5) # y will be 5
#print(y)

#z = float(5) # z will be 5.0
#print(z)

               #__________****________#
               
 # Variable name=-
 
  # 1) Camel Case=-
     
     # myVariableName = "amjad"             
 
 # 2) Pascal case=-
 
      #MyVariableName = "amjad"
      
 # 3) Snake case=-
      
            # my_variable_name = "amjad"
            
                   #________*****_______#      

  
  # Global variable=-
                      # Create a variable outside of function and used both inside & outside the function,

# Example=- 
 
#x = "awesome"

#def myfunc():
 #    print("python is "+ x)
     
#myfunc()     



# data type

# 1) python List=-
                  #List is an ordered sequence of item or element,,

  # Example=-                

#list = ["amjad","khan",10,10.9 ,45,55,55,67,99,"tufail",11,15,"amjad"]
#print(type(list),list)
#print (list)
#print (len(a))
#print (list[3])
#print(list[4:])
#print(list[:4])
#print (type(a))
#Text = "my nmae  is Amjad and i am"+ age
#age=20
#print (text.format(ag) -
#list.insert(1, "khan")
#print(list)
#list.append("javascript")
#print(list)
#list.extend("1,2,3,4,55,6,77,343,545,56,77,443,66,434,567,78,43,57,898,65,443,56,54,546,787")
#print(list)
#list.remove("amjad")
#print(list)
#list.count("list") -
#print(list)
#list.reverse()
#print(list)
#list.pop(3)
#print(list)
#list.copy() -
#print(list)
#list.sort()
#print(list)
#list [3] = "phyton"
#print(list)
#print(list[0])
#print(list[1])
#print(list[2])
#print(list[3])
#print(list[4])
#print(list[5])
#if 55 in list:
 #    print("yes 55 in present")
#list[1]="khattak"
#print(list)

# List looping

        # print all item in the list one by one:
        
        
#for x in list:
 #  print(x)        

     # print all item by referring to their index number:
     
#for i in range(len(list)):
# print(list[i])
#list1 = [1,2,3,4,55,6,77,343,545,56,77,443,66,434,567,78,43,57,898,65,443,56,54,546,787]
#list1.sort()
#print(list1)
#list2 = list1.copy()
#print(list2)
#list2 = list1 + list 
#print(list2)




                #__________********_________#

# 2)Tuple=-
         #tuple are ordered collection of data  item,,They store multiple item in a single variable,,tuple item separated by comma and enclosed in round bracket,,Tuple are unchangeable,,
         
   #Example=

#tuple=(1,2,3,4,5,6,7,8,9,10)
#tuple2=("amjad","khan","tufail","zaman")
#print(tuple1)
#print(tuple2)   
#print(type(tuple1),tuple1)         
#print(tuple1[0])
#print(tuple1[1])
#print(tuple1[2])
#print(tuple1[3])
#print(tuple1[4])
#print(tuple1[5])
#print(tuple1[6])
#print(tuple1[7])
#print(tuple1[8])
#print(tuple1[9])
#print(len(tup))
#tuple3 = tuple + tuple2
#print(tuple3)

#if 6 in tup:
     # print("yes 6 is present in tuple")      
#if 20 in tup:
 #     print("yes 20 is present in tuple")

#else:
# print("no 20 is not in tuple")

                    #_________*********__________#
        

# 3) String=-
     
         # String in python are surrounding by either single or double quotation mark,,
         
# Example=-
         #  "hello" 'hello'         

#print("Hello")

#str= "amjad","khan","tufail","rashid","arshad","sohail"
#print(str)
#print(str.count("amjad"))
#print(str.index("rashid"))
#print(len(str))
#print("amjad" in str)
#print("hafezz" in s)
#print(str[1::4])
#print(str[:4])
#print(str[3:])
#print(str[0])
#print(str[1])
#print(str[2])
#print(str[3])
#print(str[4])
#a = "  amjad kkhattak  "
#print(a.capitalize())
#print(a.upper()) 
#print(a.strip())  # strip remove any white space 
#print(a.replace("a", "m")) 
#b = a.split(",")
#print(b)
#age = 20
#txt = "My name is Amjad khan, I am" + age
#print(txt)

   #Looping throuh a string,,
 
#str1 = "Amjad khattak from karak" 
#for character in str1:
#   print(character)    
      

               #___________*****___________#


# 4) Set=-

       # set are used to multiple item in a single variable,,
       
       # set is unorderd
       # set is unchange
       # Duplicate not allowed
       
# Example=-

#set = {1,2,3,4,5,6,7,8,9,10}
#print(set)
#print(len(set))              
#print(type(set))
#print(5 in set)
#for x in set:
#   print(x)   
#set.add(11)
#print(set)
#set.remove(5)
#print(set)
#set.discard(9) -
#print(set)
#set.pop()    # Remove random item to used pop,
#print(set)
#set.clear()
#print(set)

#for x in set:  # Looop using
 #  print(x)

#set1 = {11,22,33,44,55,66,77,88}
#set3 = set.union(set1)
#print(set3)

#set.update(set1)
#print(set)

              #__________***___________#
              
              
              
# 5) Dictionary=-
                   # Dictionary are used to store data value in key value pair,,
                   # Dictionary is ordered,
                   # Dictionary is changeable, 
                   # Dictionary is duplicate not allowed,             
#Example=-

#dict = {
   
   #"name": "Amjad",
   #"frnd": "tufail",
   #"age":   "20"
      
#}

#print(dict)
#print(dict["name"])
#print(dict["age"])
#print(len(dict))
#print(type(dict))
#x = dict.get("frnd")
#print(x)
#x= dict.keys()
#print(x)
#x = dict.items()
#print(x)
#dict["age"]=22
#print(dict)
#dict.update({"age": 25})
#print(dict)
#dict.pop("name")
#print(dict)
#dict.clear()
#print(dict)

#for x in dict:   # Loooop in dict
 #  print(x)
#x = dict.copy()
#print(x)

           #___________****_________#
           
           
# Python If & Else Statement=-

#a = 33
#b = 44
#if a > b:
 #  print("a is greater than b")
#else:
   
  # print("b is greater than a")              
           
#a = 44
#b = 44
#if a > b:
 #  print("a is greater than b")
#elif a==b:
   #print("a and b are aqual") 
   
   
               #________****_________#
   
# While Loop=-

#i=1
#while i<=6:
 #  print(i)
  # i+=1
   
#i=1
#while i<6:
 #  print(i)
 #  if i==4:
  #    break   
#i+=1  
 
 
           #____________****_______#
          
             




