# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def Walk(self):
        print(f"{self.name} is Walking")
        return None

    def Talk(self):
        print("Talking")
        print(f"{self.name} is Talking ")
        return None

    def Employee_Details(self):
        print("----------Employee_Details---------")
        print(
            f" User details are :\n Name = {self.name} \n age = {self.age} \n phone = {self.phone} \n address = {self.address} \n Eid = {self.eid} ")
        return None


print("Enter details of employee 1")
name1 = input("Enter the name of employee \n")
age1 =  int(input("Enter the age of employee \n"))
phone1 = int(input("Enter the phone number of employee \n"))
address1 = input("Enter the address of employee \n")
eid1 = int(input("Enter the employee_id of employee \n"))

print("Enter details of employee 2")
name2 = input("Enter the name of employee \n")
age2 =  int(input("Enter the age of employee \n"))
phone2 = int(input("Enter the phone number of employee \n"))
address2 = input("Enter the address of employee \n")
eid2 = int(input("Enter the employee_id of employee \n"))

Employee1=Employee(name1,age1,phone1,address1,eid1)
Employee1.Walk()
Employee1.Employee_Details()

Employee2 = Employee(name2,age2,phone2,address2,eid2)
Employee2.Talk()  # ->
Employee2.Employee_Details()


"""
------------------------------------------Thinking on this ---------------------------------------
emp_count=int(input("how many employee you have :\n"))
for i in range(emp_count):
    print(f"Enter details of employee {i}")
    name = input("Enter the name of employee \n")
    age = int(input("Enter the age of employee \n"))
    phone = int(input("Enter the phone number of employee \n"))
    address = input("Enter the address of employee \n")
    eid = int(input("Enter the employee_id of employee \n"))

"""

