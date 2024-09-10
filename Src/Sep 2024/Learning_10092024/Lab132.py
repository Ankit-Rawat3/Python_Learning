#file handling
import os

"""
#code works as file exists now
file=open('example.txt','r') #FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
print(file.read())

"""
try:
    path=os.getcwd()
    print(path)
    file=open(path+'test.txt','r') #FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    print(file.read())
except FileNotFoundError as fnfe:
    print("check  the existence of file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

#positive scenario:


try:
    path=os.getcwd()
    print(path)
    file=open(path+'/example.txt','r') #FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    print(file.read())
except FileNotFoundError as fnfe:
    print("check  the existence of file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

