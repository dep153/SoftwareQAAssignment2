#David Penfield, dep153

from BMI_Calculator import BMI_Calc
from BMI_Calculator import Get_Category

while True:

    print("Which application would you like to run?")
    print("1) BMI Calculator")
    print("2) Retirement Tracker\n")

    ans = int(input("1 or 2: "))

    if ans == 1:

        print("Please input your height in feet and inches.\n")

        feet = int(input("Feet: "))
        if feet == "x":
            break

        inches = int(input("Inches: "))
        if inches == "x":
            break

        print("Please input your weight in pounds.\n")

        pounds = int(input("Pounds: "))
        if pounds == "x":
            break

        BMI = BMI_Calc(feet, inches, pounds)

        print("Your BMI is " + str(BMI) + ".")

        category = Get_Category(BMI)

        print("You are " + category + ".\n")
        
        input("Enter any value to continue: ")

    #elif ans == 2:
    #    Retire_Tracker()
