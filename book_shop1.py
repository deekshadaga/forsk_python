"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    
    Order Number    Book Title              Author      Quantity  Price per Item
    34587           Learning Python,        Mark Lutz   4           40.95
    98762           Programming Python,     Mark Lutz   5           56.80
    77226           Head First Python,      Paul Barry  3           32.95
    88112           Einführung in Python3,  Bernd Klein 3           24.99    
    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
  
    Hint:
    Write a Python program using lambda and map.
    
    # Assume the data in form of list of list
    orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

"""


def f(i):
  if(i[1]<100):
    return(i[0],i[1]+10)
  else:
    return i
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
op=list(map(f,list(map(lambda x:(x[0],round(x[2]*x[3],2)),orders))))
print(op)
