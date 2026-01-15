print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
# > gretaer than, < less than, >= greater than or equal to, <= less than or equal to, == equal to, != not equal to
#Module operator  %
print(12 % 3)  # Outputs 0 because 12 is evenly divisible by 3
print(14 % 3)  # Outputs 2 because 14 divided by 3
#number to check even or odd
number = int(input("Enter a number to check if it's even or odd: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#Nested if/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age < 18 and age >= 65:
        bill = 12
        print("Please pay $12.")
    else:
        bill = 15
        print("Please pay $15.")
    wants_photo =input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3 #add $3 to bill
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
#BMI Calculator with height and weight
weight = float(input("Enter your body weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("You are underweight")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal")
elif 25 <= bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
