import os

print(os.getcwd())
full_path_file = os.path.join("/Users/vikas\PycharmProjects\Python_Learning\Src\Sep 2024\Learning_10092024", "example.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)
