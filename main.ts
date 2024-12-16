// variable
let start = 0
let elapsed = 0
let score = 0
// Button a pressed 
function on_button_pressed_a() {
    
    // making it available all over the programme
    input.onButtonPressed(Button.A, on_button_pressed_a)
    start = input.runningTime()
    basic.showIcon(IconNames.Chessboard)
}

input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    elapsed = input.runningTime() - start
    score = Math.abs(elapsed - 7000)
    basic.showNumber(score)
})
