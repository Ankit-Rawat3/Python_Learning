### Task #11 -
#✅ Fibonaci series

num=int(input("Enter a number to create Fibonaci series : \n"))
series=[]
a,b=0,1
for i in range(num):
    series.append(a)
    a, b = b, a + b

print(f"Fibonaci series for number {num} is {series}")



