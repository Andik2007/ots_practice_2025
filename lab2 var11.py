import turtle

VERTICAL_MOVE = 100
HORIZONTAL_MOVE = 25
NUM_SEGMENTS = 9

def perform_wave_move(state, t, segments_drawn):
    if segments_drawn >= NUM_SEGMENTS:
        t.hideturtle()
        return "STOP", segments_drawn

    if state == "INIT":
        t.penup()
        t.goto(0, 0)
        t.pendown()
        return "DOWN", segments_drawn

    if state == "DOWN":
        t.setheading(270)
        t.forward(VERTICAL_MOVE)
        segments_drawn += 1
        return "RIGHT_U", segments_drawn

    if state == "RIGHT_U":
        t.setheading(0)
        t.forward(HORIZONTAL_MOVE)
        segments_drawn += 1
        return "UP", segments_drawn
    
    if state == "UP":
        t.setheading(90)
        t.forward(VERTICAL_MOVE)
        segments_drawn += 1
        return "RIGHT_D", segments_drawn

    if state == "RIGHT_D":
        t.setheading(0)
        t.forward(HORIZONTAL_MOVE)
        segments_drawn += 1
        return "DOWN", segments_drawn

    return state, segments_drawn

def draw_wave_pattern():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    
    t = turtle.Turtle()
    t.speed(3)
    t.width(3)

    segments_drawn = 0

    while curr_state != end_state:
        curr_state, segments_drawn = perform_wave_move(curr_state, t, segments_drawn)
    
    turtle.done()

if __name__ == "__main__":
    draw_wave_pattern()
