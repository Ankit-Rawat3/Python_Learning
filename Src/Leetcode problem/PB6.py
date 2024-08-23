#WAP tp convert a number to binary then convert its 0s in 1 and 1s in 0.Convert the final binary number into decimal
a=bin(5)[2:]

print(a)

y = ""
print(type(a))
for i in a:
    i=int(i)
    if (i == 1):
        b = 0
        y = y + str(b)
        print(y)
    else:
        b = 1
        y = y + str(b)
        print(y)

output = int(y,2)
print(output)