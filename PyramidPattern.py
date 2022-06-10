n=int(input("Enter a number:"))
for i in range(n):
  #for printing space 
    for j in range(n-i-1):
        print(" ", end=" ")
   #for printing stars
    for k in range(2*i+1):
        print("*", end=" ")
    print()
    
