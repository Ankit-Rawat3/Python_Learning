user_type =input("Enter the user type - admin,manager,quest \n")

match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello guest")
    case _:
        print("who are you")


