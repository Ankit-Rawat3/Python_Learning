# How to write to a file
with open('TestData.txt','a') as file:
    file.write("\t hey buddy")
    print("writing successful")