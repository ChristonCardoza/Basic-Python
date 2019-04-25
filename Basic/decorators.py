# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:19:01 2019

@author: antonc3
"""
"""---------------------------------------------------------------------------------------------------------------------------"""

def family_name(ln):
    def my_name():
        fn = "Christon"
        print(fn + ' ' +ln)
    return my_name

full_name = family_name("Cardoza")
full_name()
        
"""---------------------------------------------------------------------------------------------------------------------------"""

def decorator_fn(original_function):
    def wrapping_fn():
        print("wraper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapping_fn

def Display():
    print("display function has been executed")
    
disp = decorator_fn(Display)   
disp() 
"""---------------------------------------------------------------------------------------------------------------------------"""
def decorator_fn(original_function):
    def wrapping_fn():
        print("wraper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapping_fn

@decorator_fn
def Display():
    print("display function has been executed")
    
Display()
"""---------------------------------------------------------------------------------------------------------------------------"""
def decorator_fn(original_function):
    def wrapping_fn(*args,**kwargs):
        print("wraper executed before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapping_fn

@decorator_fn
def Display_info(name,age):
    print("display function has been executed with name:{} and age:{}".format(name,age))
    
Display_info("Christon Carddoza",23)
"""---------------------------------------------------------------------------------------------------------------------------"""