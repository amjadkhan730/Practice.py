

#Python RegEx =
           
           #A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

           #RegEx can be used to check if a string contains the specified search pattern.

          #Python has a built-in package called re, which can be used to work with Regular Expressions.

        #Import the re module:

import re


#When you have imported the re module, you can start using regular expressions:

#ExampleGet your own Python Server
#Search the string to see if it starts with "The" and ends with "Spain":



import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
  
  ###RegEx Functions
      
      #The re module offers a set of functions that allows us to search a string for a match:

       #Function	=   Description
       
       #findall	  =     Returns a list containing all matches
       
       #search    =     Returns a Match object if there is a match anywhere in the string
       
       #split	 =      Returns a list where the string has been split at each match
       
       #sub	     =       Replaces one or many matches with a string


  ###Metacharacters

         #Metacharacters are characters with a special meaning:
# 1)

# []     =     A set of charactor         =    "[a-m]" = a = 1st element & m = last element in string,

# find all lowercase charactor b/w "a" & "m":

import re

txt = "Amjad is a good boy in world"

x = re.findall("[a-m]", txt)
print(x) 


# 2)

# \	   Signals a special sequence (can also be used to escape special characters)	 "\d"

       #Find all digit characters:


import re

txt = "That will be 2023 dollars"

x = re.findall("\d", txt)
print(x)


# 3)

# .	Any character (except newline character)	"he..o"

 #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

import re

txt = "hello"

x = re.findall("he..o", txt)
print(x)



# 4)

        # ^	Starts with	"^Amjad"

  #Check if the string starts with 'Amjad':

import re

txt = "Amjad khan"


x = re.findall("^Amjad", txt)
if x:
  print("Yes, the string starts with 'Amjad'")
else:
  print("No match")
  
  
  # 5)
        # $	Ends with	"khan$"

    #Check if the string ends with 'khan':



import re

txt = "Amjad khan"


x = re.findall("khan$", txt)
if x:
  print("Yes, the string ends with 'khan'")
else:
  print("No match")
  
  
 # 6) 
  
 # *	Zero or more occurrences	"he.*o"	

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

import re

txt = "Amjadkhan"

x = re.findall("Am.*n", txt)

print(x)




# 7)

# +	One or more occurrences	"he.+o"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

import re

txt = "hello"



x = re.findall("he.+o", txt)

print(x)
