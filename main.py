#variable
start=0
elapsed=0
score=0
#Button a pressed 
def on_button_pressed_a():
    global start #making it available all over the programme
    input.on_button_pressed(Button.A, on_button_pressed_a)
    start=input.running_time()
    basic.show_icon(IconNames.CHESSBOARD)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global elapsed, score
    elapsed = input.running_time() - start
    score = abs(elapsed - 7000)
    basic.show_number(score)
input.on_button_pressed(Button.B, on_button_pressed_b)

