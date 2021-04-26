import os
import shutil
path = 'C:\\Users\\Lenovo\\Python'
print("before copying files")
print(os.listdir(path))
source = "C:\\Users\\Lenovo\\Python\\file1.txt"
destination = "C:\\Users\\Lenovo\\Python\\file2.txt"
dest = shutil.copy(source,destination)
