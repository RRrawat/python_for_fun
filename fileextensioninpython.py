#Method 1
#spilt
a = ['path1/f1/f2/file1.csv', "path1/f1/f2/file2.csv", "path3/f3/f3/file3.csv", "path4/f4/f4/file4.csv"]
b = [] 
for path in a:
    a = path.split('.', )
    a= a[1]
    b.append(a)
print(b)

#method 2
