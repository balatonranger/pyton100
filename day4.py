print(" ")
import random
#random module to generate random numbers
random_integer = random.randint(1, 10)
print(random_integer)
#random float between 0 and 1
random_float = random.random()
#random float between 0 and 1 but not including 1
print(random_float)
random_float = random.uniform(1,10)
print(random_float)
#head or tails
print(" ")
random_heads_tails = random.randint(0,1)
if random_heads_tails == 1:
    print("Heads")
else:    print("Tails")
print(" ")
states_of_america = [
    "Delaware",         # 1  (Dec 7, 1787)
    "Pennsylvania",     # 2  (Dec 12, 1787)
    "New Jersey",       # 3  (Dec 18, 1787)
    "Georgia",          # 4  (Jan 2, 1788)
    "Connecticut",      # 5  (Jan 9, 1788)
    "Massachusetts",    # 6  (Feb 6, 1788)
    "Maryland",         # 7  (Apr 28, 1788)
    "South Carolina",   # 8  (May 23, 1788)
    "New Hampshire",    # 9  (Jun 21, 1788)
    "Virginia",         # 10 (Jun 25, 1788)
    "New York",         # 11 (Jul 26, 1788)
    "North Carolina",   # 12 (Nov 21, 1789)
    "Rhode Island",     # 13 (May 29, 1790)
    "Vermont",          # 14 (Mar 4, 1791)
    "Kentucky",         # 15 (Jun 1, 1792)
    "Tennessee",        # 16 (Jun 1, 1796)
    "Ohio",             # 17 (Mar 1, 1803)
    "Louisiana",        # 18 (Apr 30, 1812)
    "Indiana",          # 19 (Dec 11, 1816)
    "Mississippi",      # 20 (Dec 10, 1817)
    "Illinois",         # 21 (Dec 3, 1818)
    "Alabama",          # 22 (Dec 14, 1819)
    "Maine",            # 23 (Mar 15, 1820)
    "Missouri",         # 24 (Aug 10, 1821)
    "Arkansas",         # 25 (Jun 15, 1836)
    "Michigan",         # 26 (Jan 26, 1837)
    "Florida",          # 27 (Mar 3, 1845)
    "Texas",            # 28 (Dec 29, 1845)
    "Iowa",             # 29 (Dec 28, 1846)
    "Wisconsin",        # 30 (May 29, 1848)
    "California",       # 31 (Sep 9, 1850)
    "Minnesota",        # 32 (May 11, 1858)
    "Oregon",           # 33 (Feb 14, 1859)
    "Kansas",           # 34 (Jan 29, 1861)
    "West Virginia",    # 35 (Jun 20, 1863)
    "Nevada",           # 36 (Oct 31, 1864)
    "Nebraska",         # 37 (Mar 1, 1867)
    "Colorado",         # 38 (Aug 1, 1876)
    "North Dakota",     # 39 (Nov 2, 1889)
    "South Dakota",     # 40 (Nov 2, 1889)
    "Montana",          # 41 (Nov 8, 1889)
    "Washington",       # 42 (Nov 11, 1889)
    "Idaho",            # 43 (Jul 3, 1890)
    "Wyoming",          # 44 (Jul 10, 1890)
    "Utah",             # 45 (Jan 4, 1896)
    "Oklahoma",         # 46 (Nov 16, 1907)
    "New Mexico",       # 47 (Jan 6, 1912)
    "Arizona",          # 48 (Feb 14, 1912)
    "Alaska",           # 49 (Jan 3, 1959)
    "Hawaii",           # 50 (Aug 21, 1959)
]
print("First state in the list:", states_of_america[0]) #first item in the list
print("Second state in the list:", states_of_america[1]) #second item in the list
print("Last state in the list:", states_of_america[-1]) #start from the end of the list

print(" ")
frends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print("Random friend:", random.choice(frends))

#nested_list
print(" ")
fruits = ["Strawberry", "Apple", "Pear"]
vegetables = ["Spinach", "Kale", "Tomato"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(fruits)
print(vegetables)

print(" ")
#rock paper scissors game
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
computer_choice = random.randint(0, 2)
choices = ["Rock", "Paper", "Scissors"]
print(f"You chose: {choices[int(user_choice)]}")
print(f"Computer chose: {choices[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "0" and computer_choice == 2) or (user_choice == "1" and computer_choice == 0) or (user_choice == "2" and computer_choice == 1):
    print("You win!")
else:    print("You lose!") 
