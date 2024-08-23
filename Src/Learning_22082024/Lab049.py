# match statement
# Switch
# match and execute
# python >3.10

"""match ank:
    case 1:
        print("A")
    case 2:
        print("B")

"""
#WAP to ask user which browser  he want to use

browser_name =input("Enter the name of browser \n")
match browser_name.lower():
    case "firefox":
        print("Execute Firefox code")
    case "chrome":
        print("Execute chrome code")
    case "edge":
        print("Execute edge code")
    case "safari":
        print("Execute safari code")
    case _:
        print("No browser found ! ")



