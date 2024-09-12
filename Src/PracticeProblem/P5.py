#word occurence
str="I am java Developer i am proud of it"
output={}
str=str.split(" ")
for i in str:
    print(i,str.count(i))
    output[i]=str.count(i)
print(output)