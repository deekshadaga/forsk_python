"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""

l=['Alabama','California','Oklahoma','Florida']
ll=[]
vowels = ('a', 'e', 'i', 'o', 'u')
for i in l:
  new=i
  for j in range(0,len(i)):
    if (i[j].lower() in vowels):
      new = new.replace(i[j],"");
  ll.append(new);
print(ll)
