"""NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices."""

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

#Your First NumPy Array
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Import the numpy package as np
import numpy as np
# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))

import numpy as np
python_list = [1,2,3]
np_array = np.array ([1,2,3])
result1 = python_list + python_list
print(result1)
#magkaiba sila ng result kase mag kaiba ng methods
result2 = np_array + np_array
print(result2)

#Lightweight baseball players
# height and weight are available as a regular lists
# Import numpy
import numpy as np
# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = bmi < 21
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

#NumPy Side Effects
import numpy as np
np_dikoalam = np.array([True, 1, 2]) + np.array([3, 4, False])
print(np_dikoalam)
#ow (1) + 3= 4 , 1 + 4 = 5, 2 + (0) = 2
# tinake yung true(1) at false(0) as integer


#Subsetting NumPy Arrays
# height and weight are available as a regular lists
# Import numpy
import numpy as np
# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)
# Print out the weight at index 50
print(np_weight_lb[50])
# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

#------------------------------------------
#2d Numpy
import numpy as np
                    #0     1    2     3    4
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79]    #0
                 ,[65.4, 59.2, 63.6, 88.4, 68.7]])  #1
shape = np_2d.shape #(2, 5)
#print the 4th column
print(np_2d[:,3])
arraymatrix = np_2d[0][2] # row 1 column 3
arraymatrix1 = np_2d[0,2] # row 1 column 3 padin ibang format lang 
arraymatrix2 = np_2d[:,1:3] # row - simula hanggang pababa
                      # column - simula sa 1 pero di dapat abot sa index 3
arraymatrix3 = np_2d[1,:] # pag gusto ko weight lang kukunin
print(np_2d)
print(shape)
print(arraymatrix)
print(arraymatrix1)
print(arraymatrix2)
print(arraymatrix3)

arraymatrix4 = np_2d[1,:1] #row 1, : starting from column 0 not including column1
print(arraymatrix4)
#[65.4]  

#Your First 2D NumPy Array
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

#Subsetting 2D NumPy Arrays
# regular list of lists
x = [["a", "b"], 
     ["c", "d"]]
result = [x[0][0], 
          x[1][0]]
print(result)


# baseball is available as a regular list of lists
# Import numpy package
import numpy as np
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)
# Print out the 50th row of np_baseball
print(np_baseball[49])
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
# Print out height of 124th player
print(np_baseball[123,0])  # 123 row 0 column 


#------------------------------------------

#2D Arithmetic
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
print(np_mat + np_mat)

# baseball is available as a regular list of lists
# updated is available as 2D numpy array
# Import numpy package
import numpy as np
# Create np_baseball (3 cols)
np_baseball = np.array(baseball)
# Print out addition of np_baseball and updated
print(np_baseball + updated)
# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])
# Print out product of np_baseball and conversion
print(np_baseball * conversion)

#------------------------------------------
#Numpy: Basic Statistics
import numpy as np
height_in =([1.73, 1.68, 1.71, 1.89, 1.79])
weight_lb =([65.4, 59.2, 63.6, 88.4, 68.7])

heightr = np.round(height_in)
weightr = np.round(weight_lb)
#normal distribution
heightr1 = np.round(np.random.normal(height_in))
weightr1 = np.round(np.random.normal(weight_lb))
complete = np.column_stack((height_in,weight_lb))
mean = np.mean(complete[:,0])
median= np.median(complete[:,0])

print(complete)
print(heightr)
print(weightr)      # horizontal rounded
print(np.column_stack((heightr,weightr))) # pa stack or vertical rounded
print(heightr1)
print(weightr1)
print(mean)
print(median)

# np_baseball is available
# Import numpy
import numpy as np
# Create np_height_in from np_baseball
np_height_in  = np.array(np_baseball[:,0])
# Print out the mean of np_height_in
print(np.mean(np_height_in))
# Print out the median of np_height_in
print(np.median(np_height_in))


# np_baseball is available
# Import numpy
import numpy as np
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height. Replace 'None'
med = np.median(np_baseball)
print("Median: " + str(med))
# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))


# heights and positions are available as lists
# Import numpy
import numpy as np
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights=np.array(heights)
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
# Heights of the other players: other_heights
other_height = np_heights[np_positions != 'GK']
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_height)))
