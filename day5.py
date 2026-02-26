#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
#    print(fruits) #prints the whole list each time, not just the current fruit
print(fruits)
print(" ")
students_scores = [78, 85, 92, 88, 95] 
print("Highest score: " + str(max(students_scores))) #prints the highest score
for score in students_scores:
    print(score)
    if score >= 90:
        print("Excellent!")
    elif score >= 80:
        print("Great job!")
    else:
        print("Keep trying!")
print(" ")
#range function
for number in range(1, 11): #11 is not included in the range, so it will print numbers from 1 to 10
    print(number)
print("")
for number in range(0, 101, 10): #prints numbers from 0 to 100 with a step of 10
    print(number)
print(" ")

total = 0
for number in range(1, 101):
    total += number
print("The sum of numbers from 1 to 100 is:", total)
print(" ")

