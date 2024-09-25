#Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.
from numpy.random import randint

orig_list=[]
new_list=[]
for i in range(20):
    orig_list.append(randint(0, 100))

for j in orig_list:
    if j%2==0:
        new_list.append(j)

print(orig_list)
print(new_list)




