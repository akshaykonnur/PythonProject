# opening a file in python
# open(file_name, modes_to_open)
# modes : r, w, x, a, t, b     => r,t are default mode
# r - read | w - write/overwrite | x - create | a - append | t - text mode | b - binary mode
'''
file_handler = open("test.txt", "rt")
print(file_handler.read())
## read operation

file_handler.close()
## close operation => close()
'''
import os

'''
# creating a file using 'x' mode

fh = open("test_01.txt", "xt")

## writing into the file
# write(content)
fh.write("This file is created using 'x' mode in python.\nsome content")
fh.write("\nNext line")

## close the file
fh.close()
'''

'''
# w mode - open the file for writing. overwrites the file
# creates a new file if file does not exist 

fh = open("test_01.txt", "wt")
fh.write("This file is overwritten using 'w' mode in python.\n")
fh.write("have a nice day")
fh.close()
'''

'''
# read operation
# read() => reads the content of the file as str
# readline() => it reads the content line by line
# readlines() => it reads the all content from the file it displays the result in list format
# content = file_handler.read(10)  => this reads first 10 characters of the file

fh = open("test_02.txt", "rt")
line_1 = fh.readlines()
# line_2 = fh.readline().strip()
# line_3 = fh.readline()
print(line_1)
for line in line_1:
    print(line.rstrip('\n'))
'''

'''
# a mode => append mode
# if the file does not exist 'a' mode creates the file

fh = open("test_02.txt", "at")
fh.write("\nThis content has been written using 'a' mode.\n")
fh.write("a mode is used to add new content at the end of the file.")
fh.write("\nGood Bye")
fh.close()
'''

'''
# with statement => it closes the file automatically
with open("test_03.txt", "xt") as fh:
    fh.write("This files is created using with statement\n")
    fh.write("Have a nice day")
'''

'''
# check file
# os.path.exists(file_name or path)

if os.path.exists("C:/Users/Dell/PycharmProjects/PythonProject/test_03.txt"):
    print("file exists")
else:
    print("file does not exist")

# pathlib.Path.exists()
# write a program to check if the file exits and if not create it with loop
from pathlib import Path
file_name = Path("C:/Users/Dell/PycharmProjects/PythonProject/test_04.txt")
if file_name.exists():
    print("file exists, cannot create new file")
else:
    print("file does not exists, creating new file")
    fh = open("test_04.txt", "xt")
    fh.write("this file is created using check statement or function")
    fh.write("\nHave a nice day")
    fh.close()
'''
