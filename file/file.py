import os


#To write to a file
handle = open("files/new.txt", "w")
handle.write("hello friends this is my first text file.\nIf you think so")
handle.close()

#To read from a specific file
handle = open("files/new.txt")
r = handle.read()
print(r)
handle.close()

#To append to a file
handle = open("files/new.txt", "a+")
handle.write("Hi")
handle.close()

#To delete a file
os.remove("files/new.txt")