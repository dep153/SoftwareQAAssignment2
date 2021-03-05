# Calculate a person's body mass index

def BMI_Calc(feet, inches, pounds):

    kilos = pounds * 0.45

    height_in_inches = (feet * 12) + inches
    meters = height_in_inches * 0.025

    BMI_exact = kilos / (meters * meters)
    BMI = round(BMI_exact, 1)

    return BMI
