s="LVIII"
n=0

for i in s:
    i=i.upper()
    match i:
        case "I":
                n=n+1
        case "L":
                n=n+50
        case "X":
                n=n+10
        case "M":
                n=n+1000
        case "V":
                n=n+5

print(n)
