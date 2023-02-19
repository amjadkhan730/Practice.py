
# Data Distribution =

                     # In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.
                     
                     #To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
                     
         #Example
                         
                         #Create an array containing 250 random floats between 0 and 5:                  

import numpy
x = numpy.random.uniform(0.0,5.0,250)
print(x)


# Scatter plot =

               # a scatter plot is a diagram where each value in the data set is represent by a Dot ,
               
               
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#The x array represents the age of each car.

#The y array represents the speed of each car.               

# Exaple 

         # Use the scatter() method to draw a scatter plot diagram:
         
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()


         

 
      



# Histogram =

             # we can represent the data in the form of diagram,,which can used python modules "matplotlib"
             
#Three lines to make our compiler able to draw:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()




             
             
             


