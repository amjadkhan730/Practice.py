
#Python Dates
#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

#Example=

#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))