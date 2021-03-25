#Familiar functions
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
# Print out type of var1
type(var1)
# Print out length of var1
len(var1)
# Convert var2 to an integer: out2
out2 = int(var2)
print(type(var1))
print(len(var1))
print(out2)

#Use help
help(max)
?max

# Multiple Argument
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first +second
# Sort full in descending order: full_sorted
full_sorted=sorted(full, reverse = False)#pag true mataas pababa, pag false mababa pataas
# Print out full_sorted
print(full_sorted)


#------------------------------------------

#Methods
#list methods
sister="loanne"
areas = [11.25, 18.0, 20.0, 20.0, 9.50,"wow","wow"]
index= areas.index(18.0)
print(index)
count=areas.count("wow")
print(count)
sister1= sister.capitalize()
print(sister1)
sister2= sister.replace("e","ers")
print(sister2)
sister3= sister.index("l")
print(sister3)


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45) #pandagdag
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse() #babaliktarin lang
# Print out areas
print(areas)


# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper() #capitalize all
# Print out place and place_up
print(place)
print(place_up)
# Print out the number of o's in place
print(place.count('o')) #count lang 


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20.0)) #pang ilan yung 0.20
# Print out how often 9.50 appears in areas
print(areas.count(9.50))


#------------------------------------------
#Packages
#Import package
# Definition of radius
r = 0.43
# Import the math package para halimbwa di na tayo mag tatype ng value ng pi math.pi lang oks na 
import math
# Calculate C
C = 2*math.pi*r
# Calculate A
A = math.pi*(r**2) #or A = math.pi*(math.pow(r,2))
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

#selective
# Definition of radius
r = 192500
# Import radians function of math package
from math import radians #if you decide to only use a specific part of a package
# Travel distance of Moon over 12 degrees. Store in dist.
phi= 12
dist = r * radians(phi)
# Print out dist
print(dist)



