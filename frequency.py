"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 

Sample Input:
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 
d1={}
s=input("enter a string: ")
for i in s:
    d1.update({i:s.count(i)})
print(d1)
