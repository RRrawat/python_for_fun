#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

# Python3 Program to
# find sum of square
# of first n natural 
# numbers
  
  
# Return the sum of
# square of first n
# natural numbers

def squaresum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm
  
# Driven Program
n = 4
print(squaresum(n))
  #Output=30
  
  
/****************************************************************************************************************************************/

#Second method

# Python3 Program to
# find sum of square 
# of first n natural 
# numbers
  
# Return the sum of 
# square of first n
# natural numbers

def squaresum(n) :
    return (n * (n + 1) * (2 * n + 1)) // 6
  
# Driven Program
n = 4
print(squaresum(n))

#Output=30  

/*****************************************************************************************************************************/
#Third method

# Python Program to find sum of square of first
# n natural numbers. This program avoids
# overflow upto some extent for large value
# of n.y
  
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
  
# main()
n = 4
print(squaresum(n));
  #Output=30
