#David Penfield, dep153

from BMI_Calculator import BMI_Calc
from BMI_Calculator import Get_Category

print("Which application would you like to run?")
print("1) BMI Calculator")
print("2) Retirement Tracker\n")

while True:

    ans = input("1 or 2: ")

    if ans == 1:

        print("Please input your height in feet and inches.\n")

        feet = input("Feet: ")
        if feet == "x":
            break

        inches = input("Inches: ")
        if inches == "x":
            break

        print("Please input your weight in pounds.\n")

        pounds = input("Pounds: ")
        if pounds == "x":
            break

        BMI = BMI_Calc(feet, inches, pounds)

        print("Your BMI is " + BMI + ".")

        category = Get_Category(BMI)
        
        print("You are " + category + ".")

    #elif ans == 2:
    #    Retire_Tracker()
