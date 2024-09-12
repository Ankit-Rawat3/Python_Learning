#Find 3rd largest number using bubble sort

a1=[1,2,3,6,10,16,0,25,7]
a2=[]
for i in a1:
    for j in a1:
        if j>=i:
            a2.append(i)
a2=list(set(a2))
print(f"third largest number is {a2[-3]}")

