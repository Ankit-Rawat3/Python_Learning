#Triangle Classifier:

length1 = int(input("Enter the length of side 1 of triangle : \n"))
length2 = int(input("Enter the length of side 2 of triangle : \n"))
length3 = int(input("Enter the length of side 3 of triangle : \n"))


if length1 ==length2 == length3:
    print(f"From {length1} ,{length2},{length3}, All sides are  equal, Hence the triangle is Equilateral  ")
elif length1 == length2!=length3 or length1 == length3!=length2 or length2 == length3!=length1:
    print(f"From {length1} ,{length2},{length3}, two sides are equal, Hence the triangle is Isosceles ")
else:
    print(f"From {length1} ,{length2},{length3}, no sides are not equal, Hence the triangle is scalene")
