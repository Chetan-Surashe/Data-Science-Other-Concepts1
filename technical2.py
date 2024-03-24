# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:42:50 2024

@author: Chetan Surashe
"""
#methods--> we are using . operator 
#       --> written inside the class
#       -->eg. s.upper()

# function--> not use . operator
#         --> can be written outside the function
#         --> paramters provided in the parenthesis
#         --> eg. len(s)

# using the methods changing the cases of string
s="welcome to sanjivani college of engineering"
print("The message is uppercase:",s.upper())
t="SANJIVANI COLLEGE OF ENGINEERING"
print("The message is lowercase:",s.lower())


# id
a=2
print(id(a)) #140734726640456
b=2
print(id(b)) #140734726640456

#Both having same id's because a & b having the same value
# so to save the memory both having the same id


nam="  Sanjivani"
print(nam) #printing with spaces
#  Sanjivani
print(nam.strip()) #printing without starting spaces
#Sanjivani

# Formatting the strings
name="Chetan"
age=21
m="my name is {} and i am {} years old".format(name,age)
n=f"my name is {name} and i am {age} years old"
print(m)
print(n)

# getting know about string
print(dir(str)) #print all the methods in string class
""" _str_ --> underscore is the special methods called 
automatically just like constructor """

print(help(str))  #detail information of the methods
 
# len is the function 
print(len(m))

#deep copy

import copy
ol=[1,[2,3],4]
dc=copy.deepcopy(ol)
print("original list:",ol)
print("deep copy: ",dc)

#replace in only deep copy list
dc[1][0]=7
print("deep copy: ",dc)
print("original list:",ol)

#appending in the deep copy
dc.append(10)
print("deep copy: ",dc)
print("original list:",ol)

# shallow copy

#shallow copy is linked with the original copy the changes
#made in the original copy is also change the shallow copy
#while deep copy maintain the separate copy and not going 
#to change as per original list

import copy
ol=[1,[2,3],4]
sc=copy.copy(ol)
print("original list:",ol)
print("shallow copy: ",sc)

#replace in only shallow copy list
sc[1][0]=7
print("shallow copy: ",sc)
print("original list:",ol)


#appending in the shallow copy
sc.append(10)
print("shallow copy: ",sc)
print("original list:",ol)

#dictionary sorting

mydict={"c":3,"a":1,"b":20}
#without lambda-->sorted sorts based on keys
print(sorted(mydict.items()))
#[('a', 1), ('b', 20), ('c', 3)]


#with lambda function
mydict={"c":3,"a":18,"b":223}
print(sorted(mydict.items(),key=lambda item:item[1]))
#here lambda is the key and item:item[1] is the first 
#key value pair & item[0]--> 1st key and item[1]-->1st value
#so we are providing the value to the key as item[1]
#so it is sorting according to value

#o/p--> [('c', 3), ('a', 18), ('b', 223)]


#creating the lambda function
mul=lambda a,b:a*b
result=mul(2,3)
print(result)

######################################3
add=lambda a,b:a+b
result=add(2,3)
print(result)
###################################
def greet():
    print("hello")
greet()
  
##################################################
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def perform_operation(operation,x,y):
    return operation (x,y)

result=perform_operation(add,5,3)
print(result)

result=perform_operation(mul,5,3)
print(result)

def square(x):
    return x*x

def compose(f,g):
    return lambda x,y:f(g(x,y))

result=compose(square,add)(2,3)
print(result)