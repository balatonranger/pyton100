def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#while loop version 6 hurdles    
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#while loop version with at_goal() function
# while not at_goal(): double negative is the same as not    
while at_goal() != True:
    jump()

#for is better for list of items, while is better for repeating until condition is met.
#while loop is better when you don't know how many times you need to repeat the code, for example, if you want to keep jumping until you reach the goal, you don't know how many jumps it will take, so while loop is better.
#infinite loop is when the condition is always true, for example, while True: will keep running forever until you stop it.
#when the wall is in different positions, you can use the front_is_clear() function to check if there is a wall in front of you, and if there is, you can jump, otherwise, you can move forward.
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#one move had to be removed from the jump function because the wall was in different positions, so the robot had to move forward before checking for the wall.
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#when is random walls are in different positions, you can use the front_is_clear() function to check if there is a wall in front of you, and if there is, you can jump, otherwise, you can move forward. This way, the robot can navigate through the maze without knowing the exact layout of the walls.

logo Reeborg's World

 
139/139

    Python Code
    library

def turn_around():

    turn_left()

    turn_left()

    

def turn_right():

    turn_left()

    turn_left()

    turn_left()

​

def jump():

    turn_left()

    while wall_on_right():

        move()

    

    turn_right()

    move()

    turn_right()

    

    while front_is_clear():

        move()

    turn_left()

    

while not at_goal():

    if wall_in_front():

        jump()

    else:

        move()

#maze find the exit with random walls in different positions, you can use the front_is_clear() function to check if there is a wall in front of you, and if there is, you can jump, otherwise, you can move forward. This way, the robot can navigate through the maze without knowing the exact layout of the walls.
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#infinit loop version, the robot will keep moving forward until it reaches the goal, if there is a wall in front of it, it will turn left and keep moving forward until it reaches the goal. This way, the robot can navigate through the maze without knowing the exact layout of the walls.
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()