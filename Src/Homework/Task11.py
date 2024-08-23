### Task #11 -
#✅ Fibonaci series

num=int(input("Enter a number to create Fibonacci series : \n"))
series=[]
a,b=0,1
for i in range(2,num+1):
    series.append(a)
    a, b = b, a + b

print(f"Fibonaci series for number {num} is {series}")



