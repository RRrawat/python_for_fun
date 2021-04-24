#1 to 50 table by Nested loops in python
for i in range(1,51):
    for j in range(i,i*10+1,i):
        print(j,end=' ')
    print()