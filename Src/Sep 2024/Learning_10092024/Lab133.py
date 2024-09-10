import os
#operating system

print(os.name) #nt

if os.name=="nt":
    print("using windows")
else:
    print("using Mac")

print(os.getcwd())
#os.chdir("/E:\Tenorshare\Firmware")
#os.mkdir('New directory')

print(os.listdir('.'))

for f in os.listdir():
    print(f)

#os.remove(Filename)
#os.rename(Filename)

#full_path= os.path.join(location1,location2)

"""
print(os.path.exists())
print(os.path.isfile())
print(os.path.isdir())
"""

# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')

"""full_path = os.path.join('/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024', 'file.txt')
# "/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/file.text"


print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))

print(os.path.isdir('directory_name'))
"""
