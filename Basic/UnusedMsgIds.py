# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:51:42 2019

@author: antonc3

"""
# importing the library 
import re

# read the file which is download from investigation EVENT COUNT
f = open('C:\\Testing_Scripts\\symanticav.txt','r')
r = f.read()
#extract the msg id     
indexmsgid = re.findall(r'msg.id=(.+?),' ,r,flags=re.DOTALL)


# read the parser xml file
g = open('C:\\Testing_Scripts\\v20_symantecavmsg.xml','r')
rd = g.read()
#extract the msg id 
msgid = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"', rd, flags=re.DOTALL)

#comapre list of extracted msg ids
unusedmsgid =[]
for i in msgid:
    if i in indexmsgid :
        pass
    else:
        unusedmsgid.append(i)
#printing the msg ids        
print("The Unused msgids are: ")
for l,m in enumerate(unusedmsgid):
    print(str(l+1) + ") " + m)
       
            