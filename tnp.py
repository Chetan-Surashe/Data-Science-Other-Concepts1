# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:21:12 2024

@author: Chetan Surashe
"""
#Tnp training

#3D arrays are the combination of the multiple 2D arrays

#create 3D array with(2,3,4)
from numpy import array


arr=array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])

print(arr)
print (arr([1][0][1]))

#[[[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]]
import numpy as np
#accesing the elememt in the 3D array
y=np.array([1,2,3,4,5])
print(y[2])


import matplotlib.pyplot as plt
# try this abbrevation
# mfc--> marker face color
# mec--> marker edge color
# ls--> linestyle

#Check for the diffenrence between taking 
#element/coordinates from array and list 

import matplotlib .pyplot as plt 

#x-axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]

#plotting the  pts
plt.plot(x,y,color='red',linestyle='dashdot'
    ,linewidth=3,marker='o',markerfacecolor='blue',
    markersize=12)
#set the y limits for the current axes
plt.ylim(1,8)
#set the x limits for the current axes
plt.xlim(1,8)
#naming the x axis
plt.xlabel('x-axis')
#naming the y axis
plt.ylabel('y-axis')
plt.title('marker graph!')
plt.legend()
plt.show()



x=np.array(["a","b","c","d"])
y=np.array([10,20,30,40])
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,y)

#pie charts in matplotlib

import pandas as pd
a=[1,2,3,4]

#TNP session 27/1/2024 by haffej sir
nam="  Sanjivani"
print(nam) #printing with spaces
#  Sanjivani
print(nam.strip()) #printing without starting spaces
#Sanjivani
name="Chetan"
age=21
m="my name is {} and i am {} years old".format(name,age)
n=f"my name is {name} and i am {age} years old"
print(m)
print(n)
print(dir(str)) #print all the methods in string class
""" _str_ --> underscore is the special methods called 
automatically just like constructor """

print(help(str))  #detail information of the methods
