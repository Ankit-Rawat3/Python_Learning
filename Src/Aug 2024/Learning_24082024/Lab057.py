#User defined function
#no return type
#No return type no argument
def greet():
    print("Hello World")

result=greet()
print(result)

#No return type with arguement

def greet_by_name(name):
    print("Hello," ,name)

greet_by_name("Ankit")

#No return type with Default arguement

def say_hello_default_arg(name="Ank"):
    print("Hello",name)

say_hello_default_arg("Hero")
say_hello_default_arg()
