import turtle,pandas

#Screen Setup
screen=turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

#states setup
data=pandas.read_csv("50_states.csv")
states_name=data.state.to_list()

right_states=[]
while len(right_states)<50:
    guess_state=screen.textinput(title=f"{len(right_states)}/50 states correct",prompt="Enter the state").title()    
    if guess_state =="Exit":
        break
    if (guess_state in states_name) and (guess_state not in right_states):
        right_raw=data[data.state==guess_state]
        right_states.append(guess_state)
        timmy=turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x=int(right_raw.x),y=int(right_raw.y))
        timmy.write(arg=guess_state,font=("Arial",10, "normal"))

my_dict={"state":[],"x":[],"y":[]}
for missed_state in states_name:
    if missed_state not in right_states:
        missed_raw=data[data.state==missed_state]
        my_dict["state"].append(missed_raw.state.item())
        my_dict["x"].append(missed_raw.x.item())
        my_dict["y"].append(missed_raw.y.item())


states_to_learn=pandas.DataFrame(my_dict)
states_to_learn.to_csv("states_to_learn.csv")



        






