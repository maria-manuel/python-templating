# print('hello templating')

print('Challenge 1 -------------')
# Challenge #1:
# This code uses Python's built-in CSV reader to read-in a CSV file
# containing the Athletic's "40 Man Roster".
# 1. If you run it right now, it will complain about "csv" not being defined.
# Add an "import statement" to get it going by importing the "csv" module from
# the Python standard library.
# 2. CSV files store "Excel-like" data -- take a look in your editor to see
# what it looks like.
# 3. Modify the code to print the name ('Name'), uniform number ('Uniform'),
# age, weight, height, and date of birth, all on one line.

# roster_file = open('athletics_40_roster.csv')
# for row in csv.DictReader(roster_file):
#     print(row['Name'])
#     print(row['Uniform'])

## Answer ##
import csv
roster_file = open('athletics_40_roster.csv')
for row in csv.DictReader(roster_file):
    print(row['Name'], row['Uniform'], row['Age'], 
    row['Weight'], row['Height'], row['Date of Birth'])


print('Challenge 2 -------------')
# Challenge #2:
# 1. Use pipenv to create a new virtualenv for this activity:
#     pipenv --python 3
# 2. "Enter" the virtualenv
#     pipenv shell
# 3. Install Pint from PyPI
#     pipenv install pint
# 4. Pint is a library for converting between different unit, such as inches
#    and meters, or pounds and kilograms. Quickly read a little about Pint:
#    https://pint.readthedocs.io/en/latest/
# 5. Each of the commented lines has a mistake. Uncomment the following code
#    and fix the mistakes to get this example test usage of Pint working:

# import(pint)
# ureg = pint UnitRegistry()
# value == 3 * ureg.meter + 4 * ureg.inches
# print value

# Answer ##
import pint
ureg = pint.UnitRegistry()
value = 3 * ureg.meter + 4 * ureg.inches
print(value)


print('Challenge 3 -------------')
# Challenge #3:
# Combine Pint with the code from Activity 1 to display all the baseball
# players' weights in kilograms.
# HINT #1: See code below
# weight_in_pounds = float(row['Weight']) * ureg.pounds
# weight_in_kilograms = weight_in_pounds.to(ureg.kilograms)
# HINT #2: If you write a new for-loop, you may need to "re-open" the file

## Answer ##
# roster_file = open('athletics_40_roster.csv')
# for row in csv.DictReader(roster_file):
#     weight_in_pounds = float(row['Weight']) * ureg.pounds
#     weight_in_kilograms = weight_in_pounds.to(ureg.kilograms)
#     print(row['Name'], row['Uniform'], row['Age']) 


print('Challenge 4 -------------')
# Challenge #4:
# Now, calculate the average weight of the baseball players, in kilograms.

total = 0
roster_file = open('athletics_40_roster.csv')
for row in csv.DictReader(roster_file):
    weight_in_pounds = float(row['Weight']) * ureg.pounds
    weight_in_kilograms = weight_in_pounds.to(ureg.kilograms)
    total = total + weight_in_kilograms

print('total weight: ', total)

print('average weight: ', total / 40) 
          

# EXTRA BONUS CHALLENGE:
# Check out the bonus_pypi_practice/ directory for the activities from last
# lesson. If you didn't have a chance to complete any of the practice
# installations from last time, now's a good time to complete them!

# OR, if you have even more time, or already completed those, you may try to do
# the Advanced Bonus Challenge, below.

print('-------------')
# Advanced Bonus Challenge:
# Use matplotlib to plot the baseball data:
# https://matplotlib.org/

# Installation: Install matplotlib with pipenv as usual, although you might
# also need to install a (system-wide) dependency known as "tkinter" to get the
# graphical graph window to pop up.

# On Linux, run (anywhere):
# sudo apt-get install python3-tk

# On macOS, run (anywhere):
# brew reinstall python --with-tcl-tk

# Code: Get going by getting the following sample code running:

#import matplotlib.pyplot as plt
#x = [10, 20, 30, 40]
#y = [10**2, 20**2, 30**2, 40**2]
#plt.scatter(x, y)
#plt.show()

