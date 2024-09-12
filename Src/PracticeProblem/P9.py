#Average of prime Number in a ranger
r= 100
a=[0,1]
for num in range(0, r + 1):
   # all prime numbers are greater than 1
   if num >= 2:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           a.append(num)
print(a)
print(f"average of prime number in range is {sum(a)/len(a)}")