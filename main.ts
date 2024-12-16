//  Variable declarations
let start = 0
let elapsed = 0
let score = 0
//  Button A pressed: Start the timer
//  Record the time when button A is pressed
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    //  Making it available throughout the program
    start = input.runningTime()
})
//  Set up button A press handler
//  Button B pressed: Calculate elapsed time and show score
//  Calculate how far the time is from 7000ms (7 seconds)
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    elapsed = input.runningTime() - start
    //  Calculate elapsed time since button A was pressed
    score = Math.abs(elapsed - 7000)
})
//  Set up button B press handler
//  Check elapsed time after the game ends
function check_time() {
    
    if (elapsed == 7000) {
        console.log("Time's up!")
    }
    
    let time_taken = 7000 - elapsed
    if (time_taken <= 0) {
        console.log("You failed!")
    } else {
        console.log(time_taken)
    }
    
}

