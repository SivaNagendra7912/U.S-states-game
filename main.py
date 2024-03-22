import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

score = 0
not_end = True

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
guessed_states = []

while not_end:
    user_state = screen.textinput(title=f"{score}/50 States Correct", prompt="what's the next state?").title()
    if score == 50:
        not_end = False

    elif user_state in states:
        guessed_states.append(user_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == user_state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(user_state)
        score += 1

    else:
        not_end = False

print(f"You guessed {score} States out of 50 states in  U.S")
missing_states = []
for state in states:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pd.DataFrame(missing_states)
new_data.to_csv("states_missed.csv")
turtle.mainloop()
