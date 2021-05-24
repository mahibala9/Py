Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Program to perform different set of operations
>>> 
>>> #define three sets
>>> E = {0, 2, 4, 6, 8};
>>> N = {1, 2, 3, 4, 5};
>>> 
>>> #set union
>>> print("Union  of E and N is",E | N)
Union  of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
>>> 
>>> #set intersection
>>> print("Intersection of E and N is",E & N)
Intersection of E and N is {2, 4}
>>> 
>>> #set difference
>>> print("Difference of E and N is",E - N)
Difference of E and N is {0, 8, 6}
>>> 
>>> #set symmetric difference
>>> print("Symmetric difference of E and N is",E ^ N)
Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
>>> 