#finding Common element in Arrays:

a1={1,2,3,2,1}
a2={1,2,3}
a3={1,2,3,4}
output=[]
print(type(a1))
print(a1)
for i in a1:
    if i in a2 and i in a3:
        output.append(i)
output=set(output)
print(output)