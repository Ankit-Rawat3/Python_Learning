def say_hello_default_arg(name="Ank"):
    print("Hello",name)

say_hello_default_arg("Hero")
say_hello_default_arg()
say_hello_default_arg(name="King")

#multiple arguement

def multiple_args(name1="Ankit",name2="ank",name3="Raw"):
    print("Multiple Arguements ", name1,name2,name3)

multiple_args()
multiple_args("ram","mohan","roy")

#Arguement + return type

def sum_of_two_number(num1,num2):
    return num1+num2

print(sum_of_two_number(5,8))
result= sum_of_two_number(5,8)
print(result)
