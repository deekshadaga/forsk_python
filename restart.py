"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""


s=input("enter a string: ")
count=s.count('r')
s=s[len(s)-1::-1].replace('r', '$',count-1)
print(s[len(s)::-1])
