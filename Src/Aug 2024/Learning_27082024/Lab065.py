def make_pizza(*toppings,base):
        print(toppings,base)
#multiple * args not allowed

#def make_pizza(*toppings,*base):
 #       print(toppings,base)


ank=make_pizza("Tomato",base="Thin crust")
ank2=make_pizza("Tomato","Onion",base="full crust")
#ank=make_pizza("Tomato","Pineapple",base="thin crust","full crust") # not allowed
ank=make_pizza("Tomato","pineapple,paneer,mushroom")