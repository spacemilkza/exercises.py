def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal:
    if right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
    move()
