import os
from os import path

filepath = os.getcwd() + "\\Reports1"
if(path.exists(filepath) == False):
   os.mkdir(filepath)
   print ("New folder created %s" % filepath)   
else:
   print ("Folder %s already exists" % filepath)   

# print ("The current working directory is %s" % path)

# define the name of the directory to be created
# path += "\\Reports"

# try:
#     os.mkdir(path)
# except OSError:
#     print ("Creation of the directory %s failed" % path)
# else:
#     print ("Successfully created the directory %s " % path)