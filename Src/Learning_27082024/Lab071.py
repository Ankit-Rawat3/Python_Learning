#Decorator

 #- used to modify the behaviour of function or class without changing its source code
 #- wrap anpther function and extend its functionality, while keeping the original function's code unchanged.

def my_decorator(func):
    #two parts
    #wrapper and cal
    def wrapper():
        print("something happening before a function call.")
        func()
        print("Something is happening after the function is called.")
    return wrapper()



@my_decorator
def drive_bike():
    print("I am riding")

def drive_scooty():
    print("Normal function - scooty")

@my_decorator
def drive_scooty():
    print("secured function- scooty")

drive_bike()
drive_scooty()