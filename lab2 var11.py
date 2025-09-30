import turtle

def perform_switch_case(state, t, turn):
    num_segments = 3      
    if state == "INIT":
        state = "DOWN"
        t.setheading(270)  
        return state, turn
        
    elif state == "DOWN":
        t.forward(100)  
        state = "RIGHT"
        t.setheading(0)  
        return state, turn
        
    elif state == "RIGHT":
        t.forward(25)  
        state = "UP"
        t.setheading(90)
        return state, turn
        
    elif state == "UP":
        t.forward(100)  
        state = "RIGHT2"
        t.setheading(0)  
        return state, turn
        
    elif state == "RIGHT2":
        t.forward(25) 
        turn += 1  
        
        if turn >= num_segments:  
            state = "FINAL_DOWN"
            t.setheading(270)  
        else:
            state = "DOWN"
            t.setheading(270)  
        return state, turn
        
    elif state == "FINAL_DOWN":
        t.forward(100)  
        state = "STOP"
        return state, turn
    
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(5)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()
