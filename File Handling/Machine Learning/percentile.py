
# Percentiles =
         
            #Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
            
    # Example =
    
              # Let's say we have an array of the ages of all the people that live in a street.
              
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages,75)
print(x)
              
                         