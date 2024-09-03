def sum_three(a=1,b=1,c=1):
    return a+b+c

result=sum_three(10,20,30)
print(result)

result2=sum_three()
print(result2)

result3=sum_three(b=10,c=10,a=100)
print(result3)


result4=sum_three(b=10,c=10,a=100,34) # - Error

print(result4)
