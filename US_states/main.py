import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# print(answer_state)

states = pd.read_csv("50_states.csv")
states_list = states["state"].tolist()
xc = states["x"].tolist()
yc = states["y"].tolist()
Game_on = True
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess another state",
                                    prompt=" What is the name of the state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        # for st in states_list:
        #     if st not in guessed_states:
        #         missing_states.append(st)
        dict = {"ms": missing_states}
        new_data = pandas.DataFrame(dict)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = states[states["state"] == answer_state]
        # t.goto(xc[states_list.index(answer_state)], yc[states_list.index(answer_state)])
        t.goto(int(state_row.x), int(state_row.y))
        t.write(f"{answer_state}", align="center", font=("calibre", 10, "normal"))

