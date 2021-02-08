# Essential Python Scripts

Hi Everyone......I'll Upload basic python tutorials.......

* * *
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjsWChPU82tln4BDeHlIWzM3yW3bYYIjBsWk2afzZ4HvJ9bsdz3Q&s"> 
</p>

> # PYTHON BASIC


> ## Features
>
>
> * Python is programming language as well as scripting language
>
> * Python is also called as Interpreted language
>
> * Object-Oriented 
>
> * Portable 
>
> * Easy to learn and use 
>
> * Mixes good features from Java, Perl and Scripting 




> ## History
>
>
>
> * Invented in the Netherlands, early 90s by Guido van Rossum 
>
> * Python implementation was started in December 1989 
>
> * Rossum published the first version of Python code (0.9.0) in February     1991
>
> * Python is derived from ABC programming language, which is a general-purpose programming language
>
> * Rossum chose the name "Python", since he was a big fan of Monty Python's Flying Circus
>
> * Open sourced from the beginning



> ### Data types
>
>
>
> * Text Type: &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; str
>
> * Set Types: &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;	set, frozenset
>
> * Boolean Type: &nbsp;&nbsp;&nbsp; &nbsp; bool
>
> * Mapping Type: &nbsp;&nbsp;&nbsp; &nbsp;dict
>
> * Binary Types: &nbsp;&nbsp; &nbsp; &nbsp;	bytes, bytearray, memoryview
>
> * Numeric Types: &nbsp;&nbsp;&nbsp; int, float, complex
>
> * Sequence Types:&nbsp;&nbsp;	list, tuple, range,String
>
>
>
>> #### Numeric Types
>>
>>
>>
>>
>> The usual suspects
>> * 12, 3.14, 0xFF, 0377, (-1+2)*3/4\**5, abs(x), 0<x<=5
>> 
>> C-style shifting & masking
>> * 1<<16, x&0xff, x|1, ~x, x^y
>> 
>> Integer division
>> * 1/2 -> 0, float(1)/2 -> 0.5
>> 
>> Long (arbitrary precision), complex
>> * 2L\**100 -> 1267650600228229401496703205376L
In Python 2.2 and beyond, 2\**100 does the same thing
>> 
>> 1j\**2 -> (-1+0j)
>
>
>
>> #### Sequence Types
>>
>>
>>
>> 1. Tuple
>>   * A simple immutable ordered sequence of items
>>   * Items can be of mixed types, including collection types
>>   * Tuples are defined using parentheses (and commas).
>>> ```python
>>> tu = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>> ```
>>   * We can access individual members of a tuple, list, or string using square bracket “array” notation. Note that all are 0 based…
>>> ```python
>>> tu = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>>
>>> tu[1] # Second item in the tuple.
>>>
>>>‘abc’
>>> ```
>> 
>>   * Positive index: count from the left, starting with 0.
>>> ```python
>>> t = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>>
>>> t[1]
>>>
>>> ‘abc’
>>> ```
>>   * Negative lookup: count from right, starting with –1
>>> ```python
>>> t[-3]
>>> 4.56
>>> ```
>>   * Return a copy of the container with a subset of the original members. Start copying at the first index, and stop copying 
>> before the second index.
>>> ```python
>>> t = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>>
>>> t[1:4]
>>>
>>> (‘abc’, 4.56, (2,3))
>>> ```
>>   * You can also use negative indices when slicing.
>>> ```python
>>> t[1:-1]
>>>
>>> (‘abc’, 4.56, (2,3))
>>>
>>> t = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>> ```
>>   * Omit the first index to make a copy starting from the beginning of the container.
>>> ```python
>>> t[:2]
>>> (23, ‘abc’)
>>> ```
>>   * Omit the second index to make a copy starting at the first index and going to the end of the container.
>>> ```python
>>> t[2:]
(4.56, (2,3), ‘def’)
>>> ```
>>   * To make a copy of an entire sequence, you can use [:].
>>> ```python
>>> t[:]
(23, ‘abc’, 4.56, (2,3), ‘def’)
>>> ```
>>   * You can’t change a tuple.
>>> ```python
>>> t = (23, ‘abc’, 4.56, (2,3), ‘def’)
>>>
>>> t[2] = 3.14
>>>
>>> Traceback (most recent call last): 
>>> File "<pyshell#75>", line 1, in -topleveltu[2] = 3.14 
>>> TypeError: object doesn't support item assignment 
>>> ```
>>   * You can make a fresh tuple and assign its reference to a previously used name.
>>> ```python
>>> t = (23, ‘abc’, 3.14, (2,3), ‘def’)
>>> ```
>>
>>
>>
>> 2. Strings
>>   * Immutable
>>   * Conceptually very much like a tuple
>>   * Strings are defined using quotes (“, ‘, or “““).
>>> ```python
>>> st = “Hello World”
>>>
>>> st = ‘Hello World’
>>>
>>> st = “““This is a multi-line
>>> 
>>> string that uses triple quotes.”””
>>> ```
>>
>>   * Strings basic operations
>>
| Python Syntax  |       Output      | Commets      |
|  :-----------------:  | :---------------:  | :-------------:   |
| "hello"+"world"|	"helloworld"| concatenation|
| "hello"*3	         | "hellohellohello" | repetition   |
| "hello"[0]	 |	"h"		         | indexing     |
|"hello"[-1]	 |	"o"		         | (from end)   |
|"hello"[1:4]	 |	"ell"		     | slicing      |
|len("hello")	 |	5		         | size         |
|"hello" < "jello"|	1		         | comparison   |
|"e" in "hello"	 |	1		        | search        |
>>
>>
>>
>> 3. List
>>
>>   * Lists are defined using square brackets (and commas).
>>> ```python
>>> li = [“abc”, 34, 4.34, 23]
>>> ```
>>   * Mutable ordered sequence of items of mixed types
>>
>>> ```python
>>> li = [‘abc’, 23, 4.34, 23]
>>> li[1] = 45
>>> li
[‘abc’, 45, 4.34, 23]
>>> ```
>>
>>   * We can change lists in place.
>>   * Name li still points to the same memory reference when we’re done.
>>   * The mutability of lists means that they aren’t as fast as tuples
>>
>>> ```python
>>> li = [1, 11, 3, 4, 5]
>>> li.append(‘a’) 
>>> li
[1, 11, 3, 4, 5, ‘a’]
>>> li.insert(2, ‘i’)
>>>li
[1, 11, ‘i’, 3, 4, 5, ‘a’]
>>> ```
>>
>>   * \+ creates a fresh list (with a new memory reference)
>>   * extend operates on list li in place.
>>
>>> ```python
>>> li.extend([9, 8, 7])
>>>li
[1, 2, ‘i’, 3, 4, 5, ‘a’, 9, 8, 7]
>>> ```
>>
>>   * Confusing:
>>     * Extend takes a list as an argument.
>>     * Append takes a singleton as an argument.
>>
>>> ```python
>>> li.append([10, 11, 12])
>>> li
>>> [1, 2, ‘i’, 3, 4, 5, ‘a’, 9, 8, 7, [10, 11, 12]]
>>>
>>> li = [‘a’, ‘b’, ‘c’, ‘b’]
>>> li.index(‘b’) # index of first occurrence
>>>1
>>>
>>> li.count(‘b’) # number of occurrences
>>>2
>>>
>>> li.remove(‘b’) # remove first occurrence
>>> li
>>> [‘a’, ‘c’, ‘b’]
>>>
>>> li = [5, 2, 6, 8]
>>> li.reverse() # reverse the list *in place*
>>> li
>>> [8, 6, 2, 5]
>>>
>>> li.sort() # sort the list *in place*
>>> li
>>> [2, 5, 6, 8]
>>>
>>> li.sort(some_function) # sort in place using user-defined comparison
>>> ```
>>
>>   * Note the difference between these two lines for mutable sequences:
>>> ```python
>>> list2 = list1 # 2 names refer to 1 ref
>>> list2 = list1[:] # Two independent copies, two refs
>>> ```
>
>
>
>> #### Dictionaries
>>
>>
>>
>>   * Dictionaries store a mapping between a set of keys and a set of values.
>>   * Keys can be any immutable type.
>>   * Values can be any type
>>   * A single dictionary can store values of different types
>>   * You can define, modify, view, lookup, and delete the key-value pairs in the dictionary.
>>
>>> ```python
>>> d = {‘user’:‘bozo’, ‘pswd’:1234}
>>> d[‘user’]
‘bozo’
>>>
>>> d[‘pswd’]
1234
>>>
>>> d[‘bozo’]
Traceback (innermost last):
File ‘<interactive input\>’ line 1, in ?
KeyError: bozo
>>>
>>> d = {‘user’:‘bozo’, ‘pswd’:1234}
>>> d[‘user’] = ‘clown’
>>> d
{‘user’:‘clown’, ‘pswd’:1234}
>>>
>>> d[‘id’] = 45
>>> d
{‘user’:‘clown’, ‘id’:45, ‘pswd’:1234}
>>>
>>> d = {‘user’:‘bozo’, ‘p’:1234, ‘i’:34}
>>> del d[‘user’] # Remove one.
>>> d
{‘p’:1234, ‘i’:34}
>>>
>>> d.clear() # Remove all.
>>> d
{}
>>>
>>> d = {‘user’:‘bozo’, ‘p’:1234, ‘i’:34}
>>> d.keys() # List of keys.
[‘user’, ‘p’, ‘i’]
>>>
>>> d.values() # List of values.
[‘bozo’, 1234, 34]
>>>
>>> d.items() # List of item tuples.
[(‘user’,‘bozo’), (‘p’,1234), (‘i’,34)]
>>> ```


> ## Whitespace
>
> * Whitespace is meaningful in Python: especially indentation and placement of newlines.
>
> * Use a newline to end a line of code.
>   * Use \ when must go to next line prematurely.
> * No braces { } to mark blocks of code in Python… Use consistent indentation instead.
>   * The first line with less indentation is outside of the block.
>   * The first line with more indentation starts a nested block
> * Often a colon appears at the start of a new block.
(E.g. for function and class definitions.)

> ## Comments
> * Start comments with # – the rest of line is ignored.
> * Can include a “documentation string” as the first line of any
new function or class that you define.
> * The development environment, debugger, and other tools use
it: it’s good style to include one.
>
>> ```python
def my_function(x, y):
'''This is the docstring. This
function does blah blah blah.''' # The code would go here...
>> ```

> ## Assignment
>
> * Binding a variable in Python means setting a name to hold a reference to some object.
>  * Assignment creates references, not copies
> * Names in Python do not have an intrinsic type. Objects have types.
>  * Python determines the type of the reference automatically based on the data object assigned to it.
> * You create a name the first time it appears on the left side of an assignment expression:
> ```python
>  x = 3
> ```
> * A reference is deleted via garbage collection after any names bound to it have passed out of scope.
> * If you try to access a name before it’s been properly created (by placing it on the left side of an assignment), you’ll get an error.
>> ```python
>> y
>>
>> Traceback (most recent call last):
>> File "<pyshell#16>", line 1, in -toplevely
>> NameError: name ‘y' is not defined
>>
>> y = 3
>> y
>>
>> 3
>> ```
> * You can also assign to multiple names at the same time.
>
>> ```python
>> x, y = 2, 3
>> x
>>
>> 2
>> y
>>
>> 3
>> ```

> ## Naming Rules
>
> * Names are case sensitive and cannot start with a number. They can contain letters, numbers, and underscores.
>
> ``` bob Bob _bob _2_bob_ bob_2 BoB ```
> * There are some reserved words:
>
> ``` and, assert, break, class, continue, def, del, elif,
> else, except, exec, finally, for, from, global, if,
> import, in, is, lambda, not, or, pass, print, raise,
> return, try, while ```

> ## Reference Semantics
>
> * There is a lot going on when we type:
> ``` x = 3 ```
>   1. First, an integer 3 is created and stored in memory. A name x is created
>   2. An reference to the memory location storing the 3 is then assigned to the name x
>   3. When we say that the value of x is 3 we mean that x now refers to the integer 3
>   4. The data 3 we created is of type integer. In Python, the datatypes integer, float, and string (and tuple) are “immutable.”
>   1. This doesn’t mean we can’t change the value of x, i.e. change what x refers to …
>
>
> * For example, we could increment x:
>> ```python
>> x = 3
>> x = x + 1
>> print x
4
>> ```
>
>
> * If we increment x, then what’s really happening is:
>   1. The reference of name x is looked up.
>   2. The value at that reference is retrieved.
>   3. The 3+1 calculation occurs, producing a new data element 4 which is assigned to a fresh memory location with a new reference.
>   4. The name x is changed to point to this new reference.
>   5. The old data 3 is garbage collected if no name still refers to it.
>
>
> * For other data types (lists, dictionaries, user-defined types), assignment works differently.
>   1. These datatypes are “mutable.”
>   2. When we change these data, we do it in place.
>   3. We don’t copy them into a new memory address each time.
>   4. If we type y=x and then modify y, both x and y are changed.
>
>
>> ```python
>> a = [1, 2, 3] # a now references the list [1, 2, 3]
>> b = a # b now references what a references
>> a.append(4) # this changes the list a references
>> print b # if we print what b references,
[1, 2, 3, 4] # SURPRISE! It has changed…
>> ```

> ## Functions
> * def creates a function and assigns it a name
> * Arguments and return types are not declared
```python 
def <name>(arg1, arg2, ..., argN):
    <statements>
     return <value>
```
> * Can define defaults for arguments that need not be passed
>> ```python 
>> def func(a, b, c=10, d=100):
>>    print a, b, c, d
>>    
>>func(1,2)
1 2 10 100
>>
>>func(1,2,3,4)
1,2,3,4
>> ```
>
>
> * All functions in Python have a return value
>   * even if no return line inside the code.
>   * Functions without a return return the special value None.
>
>
> * There is no function overloading in Python.
>   * Two different functions can’t have the same name, even if they have different arguments.
>
>
> * Functions can be used as any other data type.They can be:
>   * Arguments to function
>   * Return values of functions
>   * Assigned to variables
>   * Parts of tuples, lists, etc

> ## Control of Flow
>
> 1. if
>> ```python
>> if x == 3:
>>   print “X equals 3.”
>> elif x == 2:
>>   print “X equals 2.”
>> else:
>>   print “X equals something else.”
>> print “This is outside the ‘if’.”
>> ```
>
> 2. assertion
>> ```python
>> assert(number_of_players < 5)
>> ```
>
> 3. while
>> ```python
>> x = 3
>> while x < 10:
>>  if x > 7:
>>    x += 2
>>    continue
>>  x = x + 1
>>  print “Still in the loop.”
>>  if x == 8:
>>   break
>> print “Outside of the loop.”
>> ```
>
> 4. for
>> ```python
>> for x in range(10):
>>  if x > 7:
>>    x += 2
>>    continue
>>  x = x + 1
>>  print “Still in the loop.”
>>  if x == 8:
>>   break
>> print “Outside of the loop.”
>> ```

> ## Exceptions
>
> 1. Handeling
>
>> ```python
>> try:
>>   1 / 0
>> except Exception as e:
>>   print('That was silly!',e.data)
>> else:
>>   print('if No exception i'm fona execute')
>> finally:
>>   print('This gets executed no matter what')
>> ```
>
> 2. Raising
>
>> ```python
>>   raise Exception('This is the exception you expect to handle')
>> ```

> ## OOP's Concepts in Python
>
>
>
>> ### Class & Objects
>>
>>
>>
>> Class is here a blueprint or a template. No storage is assigned when we define a class. Objects are instances of class, which holds the data variables declared in the class and the member functions work on these class objects.
>>
>>
>>
>> ``` python
>> class Example:
>> 	def __init__(self):
>> 		print "Object created"
>> 		
>> 		# destructor
>> 		def __del__(self):
>> 		    print "Object destroyed"
>> 	
>> # creating an object
>> myObj = Example()
>> # to delete the object explicitly
del myObj
>> ```
>> ``` Object created
>> Object destroyed ```
>
>
>
>> ### Inheritance
>>
>>
>> Inheritance is one of the most important aspects of Object Oriented Programming. While programming, many a times, situations arise where we have to write a few classes with some common features and some unique, class-specific features, which include both variables and methods. In such situations, as per object oriented programming, we can take out the common part and put it in a separate class, and make all the other classes inherit this class, to use its methods and variables, hence reducing re-writing the common features in every class, again and again.The class which inherits another class is generally known as the Child class, while the class which is inherited by other classes is called as the Parent class
>>
>>
>>
>> * Less code repeatition, as the code which is common can be placed in the parent class, hence making it available to all the child classes.
>> * Structured Code: By dividing the code into classes, we can structure our software better by dividing functionality into classes.
>> * Make the code more scalable.
>>
>>
>>
>> ``` python
>> class Parent:
>>  	var1 = 1
>>  	def func1(self):
>>  	    # do something here
>>
>> class Child(Parent):
>>  	var2 = 2
>>  	def func2(self):
>>        # do something here too
>>  		# time to use var1 from 'Parent'
>>  	    myVar = Parent.var1 + 10
>>  	    return myVar
>> ```
>
>
>
>> ### Access Modifiers
>>
>>
>> There are 3 types of access modifiers for a class in Python
>> * Public
>>   * The members declared as Public are accessible from outside the Class through an object of the class.
>> * Protected
>>   * The members declared as Protected are accessible from outside the class but only in a class derived from it that is in the child or subclass.
>> * Private
>>   * These members are only accessible from within the class. No outside Access is allowed.
>>
>>
>>
>> ``` python
>> # define parent class Company
>> class Company:
>>     # constructor
>>     def __init__(self, name, proj):
>>         self.name = name      # name(name of company) is public
>>         self._proj = proj     # proj(current project) is protected
>>     
>>     # public function to show the details
>>     def show(self):
>>         print("The code of the company is = ",self.ccode)
>> 
>> # define child class Emp
>> class Emp(Company):
>>     # constructor
>>     def __init__(self, eName, sal, cName, proj):
>>         # calling parent class constructor
>>         Company.__init__(self, cName, proj)
>>         self.name = eName   # public member variable
>>         self.__sal = sal    # private member variable
>>     
>>    # public function to show salary details
>>     def show_sal(self):
>>        print("The salary of ",self.name," is ",self.__sal,)
>> 
>> # creating instance of Company class
>> c = Company("Stark Industries", "Mark 4")
>> # creating instance of Employee class
>> e = Emp("Steve", 9999999, c.name, c._proj)
>> 
>> print("Welcome to ", c.name)
>> print("Here ", e.name," is working on ",e._proj)
>> 
>> # only the instance itself can change the __sal variable
>> # and to show the value we have created a public function show_sal()
>> e.show_sal()
>> print(e.__sal)
>> e.show_sal()
>> ```
>>
>>
>>
>>> ```
>>> Welcome to  Stark Industries
>>> Here  Steve  is working on  Mark 4
>>> The salary of  Steve  is  9999999
>>> ---------------------------------------------------------------------------
>>> AttributeError                            Traceback (most recent call last)
>>> \<ipython-input-38-224b96aa40aa\> in \<module>
>>>      34 # and to show the value we have created a public function show_sal()
>>>      35 e.show_sal()
>>> ---> 36 print(e.__sal)
>>>      37 e.show_sal()
>>>
>>> AttributeError: 'Emp' object has no attribute '__sal' ```
>
>
>
> ### Method Overriding
>
>
>
>> Following conditions must be met for overriding a function:
>> 
>> * Inheritance should be there. Function overriding cannot be done within a class. We need to derive a child class from a parent class.
>> * The function that is redefined in the child class should have the same signature as in the parent class i.e. same number of parameters.
>>
>>
>>
>> ``` python
>> # parent class
>> class Animal:
>>   # properties
>> 	multicellular = True
>> 	# Eukaryotic means Cells with Nucleus
>> 	eukaryotic = True
>> 	
>> 	# function breath
>> 	def breathe(self):
>> 	    print("I breathe oxygen.")
>>     
>>   # function feed
>> 	def feed(self):
>> 	    print("I eat food.")
>> 	    
>> # child class	    
>> class Herbivorous(Animal):
>>    
>>     # function feed
>> 	def feed(self):
>> 	    print("I eat only plants. I am vegetarian.")
>> 
>> herbi = Herbivorous()
>> herbi.feed()
>> # calling some other function
>> herbi.breathe()
>> ```
>>
>>
>>
>> ``` I eat only plants. I am vegetarian.
I breathe oxygen. ```
>
>
>
> ## Method Overloading
>
>
>
>> Polymorphism is a concept of Object Oriented Programming, which means multiple forms or more than one form. Polymorphism enables using a single interface with input of different datatypes, different class or may be for different number of inputs.
>> In python, polymorphism is a way of making a function accept objects of different classes if they behave similarly.
>>
>>
>>
>> ``` python
>> len("hello")      # returns 5 as result
>> len([1,2,3,4,45,345,23,42])     # returns 8 as result
>> ```
>>
>>
>>
>> * Python doesn't support method overloading on the basis of different number of parameters in functions.
>> * To achieve method overloading we have Polymorphic Classes
>>
>>
>>
>> ``` python 
>> class Square:
>>     side = 5     
>>     def calculate_area(self):
>>         print( self.side * self.side)
>> 
>> class Triangle:
>>     base = 5
>>     height = 4
>>     def calculate_area(self):
>>         print( 0.5 * self.base * self.height)
>>
>> sq = Square()
>> tri = Triangle()
>> 
>> for(obj in (sq, tri)):
>>     obj.calculate_area()
>> #Here python doesn't care about the type of object which is calling the function hence making the class method polymorphic in nature.
>> ```
>>
>>
>> * we can also create a function which takes an object of some shape class as input and then calls the function to calculate area for it
>>
>>
>>
>> ``` python 
>> class Square:
>>     side = 5     
>>     def calculate_area(self):
>>         print( self.side * self.side)
>> 
>> class Triangle:
>>     base = 5
>>     height = 4
>>     def calculate_area(self):
>>         print( 0.5 * self.base * self.height)
>>
>> find_area_of_shape(obj):
>>     obj.calculate_area()
>> 
>> sq = Square()
>> tri = Triangle()
>> 
>> # calling the method with different objects
>> find_area_of_shape(sq)
>> find_area_of_shape(tri)
>> ```
>
>
>
> ### Operator overloading
>
>
>
>> * Operators are used in Python to perform specific operations on the given operands. 
>> * The operation that any particular operator will perform on any predefined data type is already defined in Python.
>>
>>
>> #### Mathematical Operator
>> * Below we have the names of the special functions to overload the mathematical operators in python
>>
>>
| Name	| Symbol	| Special Function |
|:-----:|:---------:|:---------------:|
| Addition	| +	| \__add__(self, other) |
| Subtraction	| - | 	\__sub__(self, other) |
| Division	| /	| \__truediv__(self, other) |
| Floor Division	| //	|\__floordiv__(self, other) |
| Modulus(or Remainder)| 	%	|\__mod__(self, other) |
| Power	| **	| \__pow__(self, other) |
>>
>>
>> #### Assignment Operator
>> * Below we have the names of the special functions to overload the assignment operators in python
>>
>>
| Name	| Symbol	| Special Function |
|:-----:|:---------:|:---------------:|
| Increment	| += |\__iadd__(self, other)|
| Decrement	| -= |\__isub__(self, other)|
| Product	| *= |\__imul__(self, other)|
| Division	| /= |\__idiv__(self, other)|
| Modulus	| %= |\__imod__(self, other)|
| Power	| **= |\__ipow__(self, other)|
>>
>>
>> #### Relational Operator
>> * Below we have the names of the special functions to overload the relational operators in python
>>
>>
| Name	| Symbol	| Special Function |
|:-----:|:---------:|:---------------:|
| Less than	| < |\__lt__(self, other) |
| Greater than	| > |\__gt__(self, other) |
| Equal to	| == |\__eq__(self, other) |
| Not equal	| != |\__ne__(self, other) |
| Less than or equal to	| <= |\__le__(self, other) |
| Greater than or equal to	| > = |\__gt__(self, other) |
>>
>>
>> #### Can + Operator Add anything?
>> The answer is No, it cannot. Can you use the + operator to add two objects of a class. The + operator can add two integer values, two float values or can be used to concatenate two strings only because these behaviours have been defined in python.
>>
>>
>>
>> ``` python 
>> class Complex:
>>     def __init__(self, r, i):
>>         self.real = r
>>         self.img = i
>> 
>> c1 = Complex(5,3)
>> c2 = Complex(2,4)
>> print("sum = ", c1+c2)
>> ```
>>
>>
>>
>> ```
>> ---------------------------------------------------------------------------
>> TypeError                                 Traceback (most recent call last)
>> \<ipython-input-44-06d40a3a3365> in \<module>
>>       6 c1 = Complex(5,3)
>>       7 c2 = Complex(2,4)
>> ----> 8 print("sum = ", c1+c2)
>> 
>> TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
>> ```
>>
>>
>>
>>
>> ``` python
>> class Complex:
>>     # defining init method for class
>>     def __init__(self, r, i):
>>         self.real = r
>>        self.img = i
>> 
>>     # overloading the add operator using special function
>>     def __add__(self, sec):
>>         r = self.real + sec.real
>>         i = self.img + sec.img
>>         return complex(r,i)
>> 
>>     # string function to print object of Complex class
>>     def __str__(self):
>>         return str(self.real)+' + '+str(self.img)+'i'
>> 
>> c1 = Complex(5,3)
>> c2 = Complex(2,4)
>> print("sum = ",c1+c2)
>> ```
>>
>>
>>
>> ```
>> sum =  (7+7j)```

