#Decorator

 #- used to modify the behaviour of function or class without changing its source code
 #- wrap anpther function and extend its functionality, while keeping the original function's code unchanged.

def add_before_UI_after_UI(func):
    #two parts
    #wrapper and cal
    def wrapper():
        print("1.Before running the UI TC.")
        print("Start browser")
        func()
        print("after the UI end")
        print("Quit the browser.")
    return wrapper()



@add_before_UI_after_UI
def test_ui():
    print("I will test UI")
