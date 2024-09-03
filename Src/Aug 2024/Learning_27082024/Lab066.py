#Function scope

global_b=12 # global variable

def my_func():
    a=10 #local variable-within a func
    print(a)
    print(global_b)

def f1():
    print(global_b)
#print(a) - not allowed

my_func()
print(global_b)