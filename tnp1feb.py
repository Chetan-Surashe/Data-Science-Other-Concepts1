# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:12:44 2024

@author: Chetan Surashe
"""

#1. Write a function that takes a list of numbers as input and returns the sum of the even 
#numbers in the list.
 
numbers_list = []
def sum_of_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    sum_even = sum(even_numbers)
    return sum_even
n=int(input("Enter the list size: "))
for i in range(0,n):
    ip=int(input("Enter the numbers in the list: "))
    numbers_list.append(ip)
    

result = sum_of_even_numbers(numbers_list)
print("Sum of even numbers:", result)


#2. Write a function that takes a list of words as input and returns the longest word in the list
def find_longest_word():
    l1=[]
    wc=int(input("Enter the number of words in the list: "))
    for i in range (0,wc):
        words=input("Enter the words: ")
        l1.append(words)
    longest_word=l1[0]
    for i in l1:
        if len(i)>len(longest_word):
            longest_word=i
    return longest_word
result1=find_longest_word()
print("The longest word in the list is: ",result1)


#3. Write a function that takes a list of characters as input and removes all duplicate characters 
#from the list.
l2=[]
wc1=int(input("Enter the number of words in the list: "))
for i in range (0,wc1):
    words1=input("Enter the words: ")
    l2.append(words1)
    
result3= list(set(l2))
print("The list after removing the redundent chars.: ",result3)

#4. Write a program that takes a list of numbers as
# input and sorts the list in ascending order
numbers_list=[]
n=int(input("Enter the list size: "))
for i in range(0,n):
     ip=int(input("Enter the numbers in the list: "))
     numbers_list.append(ip)
     
result=sorted(numbers_list)
print("The ascending order list is: ",result)


#5. Write a program that takes a list of words as 
#input and reverses the order of the words in the list. 
l1=[]
wc=int(input("Enter the number of words in the list: "))
for i in range (0,wc):
    words=input("Enter the words: ")
    l1.append(words)
result=list(l1[::-1])
print(result)

#######################################################

######Tuples ###################
#1. Write a function that takes a tuple of numbers
# as input and returns the average of the 
#numbers in the tuple. 

def calculate_average(numbers_tuple):
    if not numbers_tuple:
        return None 

    total_sum = sum(numbers_tuple)
    average = total_sum / len(numbers_tuple)
    return average
numbers_tuple = (10, 15, 20, 25, 30)
result = calculate_average(numbers_tuple)
print("Average:", result)

#2. Write a funcƟon that takes a tuple of characters as input and returns the number of vowels 
#in the tuple. 
def count_vowels(characters_tuple):
    vowels = "aeiouAEIOU"
    return sum(1 for char in characters_tuple if char in vowels)


characters_tuple = ('a', 'b', 'e', 'i', 'o', 'u', 'A', 'B', 'C')
result = count_vowels(characters_tuple)
print("Number of vowels:", result)

#3. Write a program that takes a tuple of numbers as input and finds the maximum and 
#minimum values in the tuple. 
def find_max_min(numbers_tuple):
    if not numbers_tuple:
        return None, None  

    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)
    return maximum, minimum

numbers_tuple = (10, 5, 20, 15, 30)
max_value, min_value = find_max_min(numbers_tuple)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#4. Write a program that takes a tuple of words as input and prints each word in the tuple in 
#reverse order.
def reverse_words(words_tuple):
    for word in words_tuple:
        print(word[::-1])

words_tuple = ('Python', 'TNP', 'Training')
reverse_words(words_tuple)

#5. Write a program that takes a tuple of characters as input and checks if the tuple is a 
#palindrome.
def is_palindrome(characters_tuple):
    reversed_tuple = characters_tuple[::-1]
    return characters_tuple == reversed_tuple

characters_tuple = ('r', 'a', 'c', 'e', 'c', 'a', 'r')
result = is_palindrome(characters_tuple)
print("Is palindrome:", result)




