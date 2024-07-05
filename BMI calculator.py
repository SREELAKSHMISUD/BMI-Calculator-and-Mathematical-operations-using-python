#mathetmatical operations
#pemdas parenthesis(), exponents**, multiplication *, division /, addition +, subtraction -
# /&* , +&- are equal in priority
print(3*3+3/3-3) #calc from left to right

#BMI Calculator
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

weight_as_int= int(weight)
height_as_float=float(height)
bmi=weight_as_int/height_as_float ** 2 #using exponent operator
#or using multiplication and PEMDAS
bmi=weight_as_int/(height_as_float*height_as_float)
bmi_as_int =int(bmi)
print(bmi_as_int)
