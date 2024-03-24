# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:09:29 2024

@author: Chetan Surashe
"""
def log_function_call(func):
    # This is the decorator 
    
    def wrapper(*args, **kwargs):
        print(f"calling function {func.__name__}")
        print(f"arguments: {args}, {kwargs}")
        
        result = func(*args, **kwargs)  # Call the decorated function here
        return result
    
    return wrapper

def add_numbers(a, b):
    print("inside add numbers")
    return a + b

@log_function_call
def add_and_multiply(a, b, c, **kwargs):
    result = add_numbers(a, b)
    result *= c
    return result

result = add_and_multiply(4, 5, 5, multiplier=2)
print(f"Result = {result}")
