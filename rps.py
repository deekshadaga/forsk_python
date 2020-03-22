"""
Make a game of rock, paper scissors against the computer. 
Algorithm
    Tell user to enter either rock,paper or scissors
    Get the response
    Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
    Compare user selection and computer selection
    Display who wins.

Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    Make an enumerated variable type to store choices.
"""

import random
l=['rock','paper','scissors']
check=1
score1=0
score2=0
while(check!=2):
  a=random.choice(l)
  b=input("enter you choice (rock,paper,scissors) --> ")
  print('computer choice is:',a)
  if(b not in l):
    print('invalid choice!')
  elif(a==b):
    print('try again as this one is a tie!' )
  elif(a=='rock' and b=='paper'):
    print('you won!')
    score1+=1
  elif(a=='rock' and b=='scissors'):
    print('computer won!')
    score2+=1
  elif(a=='paper' and b=='scissors'):
    print('you won!')
    score1+=1
  elif(a=='paper' and b=='rock'):
    print('computer won!')
    score2+=1
  elif(a=='scissors' and b=='rock'):
    print('you won!')
    score1+=1
  elif(a=='scissors' and b=='paper'):
    print('computer won!')
    score2+=1
  check=int(input("choose: \n1)play again \n2)exit\n"))
print('your score is :',score1)
print('computer score is :',score2)
