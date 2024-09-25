#WAP(function) to accept a list and return list with distinct element from first list

def input_list():
    a=[]
    b=[]
    y="Y"
    #while(y=="Y"):
    for i in range(5):
        a.append(input("Enter the element \n"))
        #y=input("Do you want to insert more element Y/N :\n ")
    return a

b=list(set(input_list()))
print(b)
