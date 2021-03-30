import logging
from random import randint
from time import sleep
from turtle import Turtle, Screen

logging.basicConfig(level = logging.DEBUG)

players = \
    [
        { 'name': 'Ronny', 'color': 'red' },
        { 'name': 'Ginny', 'color': 'green' },
        { 'name': 'Bevin', 'color': 'blue' },
        { 'name': 'Clive', 'color': 'cyan' },
        { 'name': 'Pauly', 'color': 'purple' },
        { 'name': 'Other', 'color': 'orange' }
        ]

line_location = 220

def draw_finish_line():
    bob = Turtle()
    bob.penup()
    bob.goto(x = line_location, y = 200)
    bob.setheading(to_angle = 270)
    bob.pensize(width = 5)
    bob.pendown()
    for dash in range(17):
        bob.forward(distance = 12)
        bob.penup()
        bob.forward(distance = 12)
        bob.pendown()


def init_race():
    y_pos = 160

    scr = Screen()
    scr.setup(width = 500, height = 400)

    draw_finish_line()

    for player in players:
        player['turtle'] = Turtle(shape = "turtle")
        player['nickname'] = player['name'].lower()[:1]
        player['turtle'].shapesize(2)
        player['turtle'].color(player['color'])
        player['turtle'].penup()
        player['turtle'].goto(x = -230, y = y_pos)
        y_pos -= 60

    user_bet = scr.textinput( \
        title = "Pick the winner",
        prompt = "who is going to win"
        ).lower()[:1]

    for player in players:
        if player['nickname'] == user_bet:
            user_bet = player['name']

    return (scr, user_bet)

def race():
    while True:
        distance = randint(5,20)
        player_number = randint(0,len(players) -1)
        players[player_number]['turtle'].forward(distance)
        if players[player_number]['turtle'].xcor() >= line_location -20:
            return players[player_number]


scr, user_bet = init_race()
result = race()

def end_race(screen):
    screen.bye()

print(f"The winner is {result['name']}")
print(f"you chose {user_bet}")
if {result['name']} == {user_bet}:
    print("Well done, you win !!!")
else:
    print("Better luck next time.")

sleep(5)
scr.bye()


# logging.debug(stuff)
