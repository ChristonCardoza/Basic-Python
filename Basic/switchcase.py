# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:49:36 2019

@author: antonc3
"""

"""---------------------------------------------------------------------------------------------------------------------------"""
def equation (operator,x,y):
    switch={
                'add': lambda: x+y,
                'sub': lambda: x-y,
                'mul': lambda: x*y,
                'div': lambda: x/y,
            }
    return switch.get(operator,lambda:None)()
    
a = equation('add',2,4)   
b = equation('sub',2,4) 
c = equation('mul',2,4)
d = equation('div',2,4)
e = equation('default',2,4) 
print(equation('add',2,4))
print(equation('sub',2,4))
print(equation('mul',2,4))
print(equation('div',2,4))
"""---------------------------------------------------------------------------------------------------------------------------"""
# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
    switcher = { 
        0: 5+3, 
        1: "one", 
        2: "two", 
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 
  
# Driver program 
if __name__ == "__main__": 
    argument=3
    print (numbers_to_strings(argument))
"""---------------------------------------------------------------------------------------------------------------------------"""
