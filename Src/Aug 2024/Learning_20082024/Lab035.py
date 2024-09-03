#wap to calculate and displays Letter Grade
#For a given score(E.g A,B,C,D,F)

#A:90-100
#B:80-99
#C:70-79
#D:60-69
#F:0-59

#Logic building Formula
#user input -> Score -> int
# O/P -? Str -> A or B ...

score = int(input("Enter your score \n"))
grade = "F"
#score >=90 and score <=100 -> "A"
#score >=80 and score <=89 -> "A"

if (score >= 90) and score <= 100:
    grade = "A"
    print("Your Grade is : ", grade)
elif (score >= 80) and score <= 89:
    grade = "B"
    print("Your Grade is : ", grade)
elif (score >= 70) and score <= 79:
    grade = "C"
    print("Your Grade is : ", grade)
elif (score >= 60) and score <= 69:
    grade = "D"
    print("Your Grade is : ", grade)
elif score > 100:
    print("You are Amazing")
else:
    print("Your Grade is : ", grade)

