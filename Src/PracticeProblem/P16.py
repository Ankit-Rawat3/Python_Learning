#WAP(function) to accept a string and counts number of upper and lower case letters

def count_upper_lowercase(s):
    count_upper=0
    count_lower=0
    for i in s:
        if i.isupper():
            count_upper=count_upper+1
        else:
            count_lower=count_lower+1
    return count_upper,count_lower



s=("As he crossed Toward the PharmAcy at tHe Corner he invVluntSriLy tUrnEd hIs hEad bEcaUse of a bURst Of lIgHt tHAt hAd riCOchETed frOMm his tEMPle, and SAW, "
   "with that quick smile with which we greet a rainbow or a rose, a blindingly white parallelogram of sky being unloaded from the van—a dresser with mirrors across"
   " which, as across a cinema screen, passed a flawlessly clear reflection of boughs sliding and swaying not arboreally, but with a human vacillation, produced" 
   "by the nature of those who were carrying this sky, these boughs, this gliding façade")

a,b=count_upper_lowercase(s)
print(f" In string {s} : \n the number of Uppercase letter are :{a} \n the number of lowercase letter are {b}")
