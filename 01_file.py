# use open function to read the content of a file
f = open("sample.txt","r") # or f = open("sample.txt")
# content = f.read()
# print(content)
data = f.read(5) # read first 5 characters 
print(data)
f.close()