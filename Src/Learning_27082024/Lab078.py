import math


"""def power(num):
    return math.pow(num,2)

res=power(10)
print(res)
"""
op2=lambda num: math.pow(num,2)
op3=lambda num: math.pow(int(input("Enter a number")),2)

print(op2(10))
print(op3(11))
