
#subsetting lists of lists
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[0][1])
print(x[0][0])
print(x[-1][1])


areas = [["hallway", 11.25], 
         ["kitchen", 18.0],
         ["living room",20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
print(areas[-1][1])

#manipulating lists
x=["a","b","c"]
y=list(x)
#y=x[:]
y[1]="z"
print(x)
print(y)

#extend list
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
print(y)

#delete list element
x = ["a", "b", "c", "d"]
del(x[1])
print(x)

x=["a","B", "C"]
print(x[:])


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage" , 15.45]
#print(areas)
print(areas_1)
print(areas_2)
del(areas[-4:-2])
print(areas)


#inner working list 
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
areas_copy[0] = 5.0
print(areas)

#familiar functions
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

#list methods
sister="loanne"
areas = [11.25, 18.0, 20.0, 20.0, 9.50,"wow"]

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


# Definition of radius
r = 0.43
# Import the math package
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
from math import radians
# Travel distance of Moon over 12 degrees. Store in dist.
phi= 12
dist = r * radians(phi)
# Print out dist
print(dist)


#Numpy
import numpy as np 
height=([1.73, 1.68, 1.71, 1.89, 1.79])
weight=([65.4, 59.2, 63.6, 88.4, 68.7])
np_height = np.array(height)
np_weight = np.array(weight)
bmi= np_weight/np_height**2
print(bmi)
print(bmi[1]) # kapag gusto ng specific element
print(bmi>23) # papaalam kung yung mga list ba e true or false na > 23 
print(bmi[bmi > 23]) # anong value yung nag true


import numpy as np
python_list = [1,2,3]
np_array = np.array ([1,2,3])
result1 = python_list + python_list
print(result1)
#magkaiba sila ng result kase mag kaiba ng methods
result2 = np_array + np_array
print(result2)

# Import numpy
import numpy as np
height_in =([1.73, 1.68, 1.71, 1.89, 1.79])
weight_lb =([65.4, 59.2, 63.6, 88.4, 68.7])
# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254
# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592
# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2
# Print out bmi
print(bmi)
# Print out the weight at index 50
print(np_weight_kg[1])



import numpy as np
np_dikoalam = np.array([True, 1, 2]) + np.array([3, 4, False])
print(np_dikoalam)
#ow (1) + 3= 4 , 1 + 4 = 5, 2 + (0) = 2
# tinake yung true(1) at false(0) as integer


#2d Numpy
import numpy as np
                    #0     1    2     3    4
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79]    #0
                 ,[65.4, 59.2, 63.6, 88.4, 68.7]])  #1
shape = np_2d.shape
#print the 3rd column
print(np_2d[:,3])
arraymatrix = np_2d[0][2] # row 1 column 2
arraymatrix1 = np_2d[0,2] # row 1 column 2 padin ibang format lang 
arraymatrix2 = np_2d[:,1:3] # row - simula hanggang pababa
                      # column - simula sa 1 pero di dapat abot sa index 3
arraymatrix2 = np_2d[1,:] # pag gusto ko weight lang kukunin
print(np_2d)
print(shape)
print(arraymatrix)
print(arraymatrix1)
print(arraymatrix2)

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]



# Import numpy
import numpy as np
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
shape = np_baseball.shape
print(shape)


# regular list of lists
x = [["a", "b"], 
     ["c", "d"]]
result = [x[0][0], 
          x[1][0]]
print(result)

# numpy
import numpy as np
     # 0   1
x = [["a", "b"], # 0
     ["c", "d"]] # 1
np_x = np.array(x)
result = np_x[:,0]
print(result)

#2d arithmetic

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
print(np_mat + np_mat)
