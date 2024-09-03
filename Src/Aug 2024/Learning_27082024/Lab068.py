public_toilet="PB"

def home():
    private_toilet="PT"
    #print(public_toilet) # this become private
    print(private_toilet)
    public_toilet="LPB"
    print(public_toilet)

home()

def stranger():
    print(public_toilet)
    #print(private_toilet) #not allowed

print(public_toilet)

