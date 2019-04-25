# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:41:43 2019

@author: antonc3
"""
"""---------------------------------------------------------------------------------------------------------------------------"""
class raper:
    
    def __init__(self,name,age):
        self.name= name
        self.age = age
        
    def __repr__(self):
        return "My Name is {} and my age is {}".format(self.name,self.age)
    
    
cs = raper('Christon Cardoza',23)
"""---------------------------------------------------------------------------------------------------------------------------"""
class raper:
    
    def __init__(self,name,age):
        self.name= name
        self.age = age
        
    def __str__(self):
        return "My Name is {} and my age is {}".format(self.name,self.age)
    
    
cs = raper('Christon Cardoza',23)
"""---------------------------------------------------------------------------------------------------------------------------"""
class raper:
    
    def __init__(self,name,age):
        self.name= name
        self.age = age
        
    def __add__(self,other):
        return self.age + other.age 
    
    
a1 = raper('Christon Cardoza',23)
a2 = raper('Clinton Cardoza',23)   

print(a1+a2)
"""---------------------------------------------------------------------------------------------------------------------------"""
    
    
    
