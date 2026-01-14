#"Hello" string  [] number 0 character
print("Hello"[0])
#Integer = whole number
print(123 + 345)
#Large Integer
print(123_456_789 + 987_654_321)
#Float = decimal number
print(3.14159)
#Boolean = True or False
print(True)
print(False)
#len can be sting but not integer
print(len("Hello"))
#type() to check data type
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))
#type conversion
print(int("123") + int("456"))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 2)
#only removing the decimal without rounding
print(6 // 2)
#two asterisks is exponentiation
print(2**3)
#PEMDAS - Parentheses Exponents Multiplication Division Addition Subtraction
# ()
# **
# * or /
# + or -
print(3 * 3 + 3 / 3 -3)
#BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
#floor the bmi to whole number
print(int(bmi))
#round the bmi to nearest whole number
print(round(bmi))
#round the bmi to 2 decimal places
print(round(bmi, 2))
#f-string for formatted string
print(f"Your BMI is {bmi:.2f}")