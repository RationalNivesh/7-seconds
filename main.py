# Variable declarations
start = 0
elapsed = 0
score = 0

# Button A pressed: Start the timer
def on_button_pressed_a():
    global start  # Making it available throughout the program
    start = input.running_time()  # Record the time when button A is pressed
    

input.on_button_pressed(Button.A, on_button_pressed_a)  # Set up button A press handler

# Button B pressed: Calculate elapsed time and show score
def on_button_pressed_b():
    global elapsed, score
    elapsed = input.running_time() - start  # Calculate elapsed time since button A was pressed
    score = abs(elapsed - 7000)  # Calculate how far the time is from 7000ms (7 seconds)


input.on_button_pressed(Button.B, on_button_pressed_b)  # Set up button B press handler

# Check elapsed time after the game ends
def check_time():
    global elapsed
    if elapsed == 7000:
        print("Time's up!")
    time_taken = 7000 - elapsed
    if time_taken <= 0:
        print("You failed!")
    else:
        print(time_taken)  # Output the remaining time

# Note: The check_time function can be called after you press button B, based on the game's rules.
