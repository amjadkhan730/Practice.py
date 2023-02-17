
 #Python File Open=
            
            #File handling is an important part of any web application.

           #Python has several functions for creating, reading, updating, and deleting files.

#File Handling=

         # The key function for working with files in Python is the open() function.

         #The open() function takes two parameters; filename, and mode.

        # There are four different methods (modes) for opening a file:

        #"r" - Read - Default value. Opens a file for reading, error if the file does not exist

         #"a" - Append - Opens a file for appending, creates the file if it does not exist

        #"w" - Write - Opens a file for writing, creates the file if it does not exist

        #"x" - Create - Creates the specified file, returns an error if the file exists

      #In addition you can specify if the file should be handled as binary or text mode
      
      
      
               #"t" - Text - Default value. Text mode

              #"b" - Binary - Binary mode (e.g. images)

 #Syntax
      
      #To open a file for reading it is enough to specify the name of the file:

      #f = open("demofile.txt")
     
     #The code above is the same as:

     #f = open("demofile.txt", "rt")
   
   #Because "r" for read, and "t" for text are the default values, you do not need to specify them.

    #Note: Make sure the file exists, or else you will get an error.
    
f = open("demofile.text", "r")
print(f.read())

 #Return the 5 first characters of the file:

f = open("demofile.text", "r")
print(f.read(5))

 #You can return one line by using the readline() method:
 
f = open("demofile.text","r")
print(f.readline())
 
#Loop through the file line by line: 
 
f = open("demofile.text", "r")

for x in f:
   print(x)
   
#Close the file when you are finish with it:

f = open("demofile.text","r")
print(f.read())
f.close()
   
   
   
                               #### python file writte & create ###


  #To write to an existing file, you must add a parameter to the open() function:

   #"a" - Append - will append to the end of the file

   #"w" - Write - will overwrite any existing content   
   
# Example=
    
        # Open the file "demofile2.txt" and append content to the file:
        
f = open("demofile.text", "a")
f.write("Amjad khan khattak") 
f.close()
#open and read the file after the appending:
f = open("demofile.text","r")
print(f.read())       
           
           
   #Open the file "demofile3.txt" and overwrite the content:   
   #Note: the "w" method will overwrite the entire file.     
   
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:

f = open("demofile3.txt", "r")
print(f.read())
 
 
 ##### Create a New File=
      
      #To create a new file in Python, use the open() method, with one of the following parameters:

    #"x" - Create - will create a file, returns an error if the file exist

    #"a" - Append - will create a file if the specified file does not exist

    #"w" - Write - will create a file if the specified file does not exist
    
  #Create a file called "myfile.txt":
    
f = open("myfile.text","x")    

#Result: a new empty file is created!


#Create a new file if it does not exist:

f = open("myfile.txt", "w")



##### Delete a File=
     
                #To delete a file, you must import the OS module, and run its os.remove() function:

 #Example
                
                #Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

#Check if file exists, then delete it:

import os
if os.path.exists("demofile.text"):
     os.remove("demofile.txt")
else:
    print("the file dosnt exist")
    
    
    ### Delete Folder =
                
                #To delete an entire folder, use the os.rmdir() method:


                #Remove the folder "myfolder":

import os
os.rmdir("myfolder")

                         #Note: You can only remove empty folders.

