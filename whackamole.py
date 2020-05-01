#Project Whack-a-mole

import nyan
from random import randint
import pygame

nyan.set_backdrop('light blue')
pygame.display.set_caption("Whack-a-mole")

gamemode_button_rect = nyan.new_rect(color = 'yellow', x = -150, y = -150, width = 150, height = 50)
gamemode = 'Whackamole'
gamemode_txt = nyan.new_text(text = str(gamemode), x = -150, y = -150, font_size = 35)

score_num = 0
scorenum_txt = 0

hitext = nyan.new_text(text = 'This is Whack-A-Mole!', x = 0, y = nyan.screen.top - 50, font_size = 40)
byetext = nyan.new_text(text = 'Your time is out. Your score was: ' + str(score_num), x = 0, y = -150, font_size = 40)
byetext.hide()

timer = nyan.new_text(text= 'Time left: ', x = nyan.screen.right - 120, y = nyan.screen.top-40, font_size=40)
timernum = 60
timernumtext = nyan.new_text(text = str(timernum), x = nyan.screen.right - 40, y = nyan.screen.top - 40, font_size = 40)

start_button_rect = nyan.new_rect(color = 'red', x = 0, y = -150, width = 75, height = 50)
start_button = nyan.new_text(text = 'Start', x = 0, y = -150, font_size = 40)

retry_button_rect = nyan.new_rect(color = 'red', x= -300, y = -150, width = 75, height = 50)
retry_button = nyan.new_text(text = 'Retry', x = -300, y = -150, font_size = 40)
retry_button.hide()
retry_button_rect.hide()

menu_button_rect = nyan.new_rect(color = 'red', x = 300, y = -150, width = 75, height = 50)
menu_button = nyan.new_text(text = 'Menu', x = 300, y = -150, font_size = 40)
menu_button.hide()
menu_button_rect.hide()

difficulty = 0.6
difficulty_txt = nyan.new_text(text = 'Difficulty: ', x = 0, y = -200, font_size=40)
difficulty_rect = nyan.new_rect(color = 'red', x = 125, y = -200, width = 75, height = 50)
difficulty_txt2 = nyan.new_text(text = 'Hard', x = 125, y = -200, font_size = 40)

hole1 = nyan.new_circle(color = 'black', x = -100, y = 40, radius = 25, border_color='blue', border_width=2)
hole2 = nyan.new_circle(color = 'black', x = 0, y = 40, radius = 25, border_color='blue', border_width=2)
hole3 = nyan.new_circle(color = 'black', x = 100, y = 40, radius = 25, border_color='blue', border_width=2)
hole4 = nyan.new_circle(color = 'black', x = -100, y = -40, radius = 25, border_color='blue', border_width=2)
hole5 = nyan.new_circle(color = 'black', x = 0, y = -40, radius = 25, border_color='blue', border_width=2)
hole6 = nyan.new_circle(color = 'black', x = 100, y = -40, radius = 25, border_color='blue', border_width=2)

holes = []
holes.append(hole1)
holes.append(hole2)
holes.append(hole3)
holes.append(hole4)
holes.append(hole5)
holes.append(hole6)

catchahole = nyan.new_circle(color = 'black', x = 0, y = 0, radius = 25, border_color = 'blue', border_width = 2)
catchahole.hide()

game = False

@nyan.when_program_starts
async def start():
    global scorenum_txt
    global timernum
    global timernumtext
    global score_num

    score_txt = nyan.new_text(text = 'Score: ', x = nyan.screen.right - 120, y = nyan.screen.top - 80, font_size = 40)
    score_num = 0
    scorenum_txt = nyan.new_text(text = str(score_num), x = nyan.screen.right - 40, y = nyan.screen.top - 80, font_size = 40)

@nyan.repeat_forever
async def do():
    global scorenum_txt
    global score_num
    global timernum
    global timernumtext
    global game
    global byetext

    if game == True:
        await nyan.sleep(seconds=1)
        timernum -= 1
        timernumtext.text = str(timernum)

        if timernum == 0:
            game = False
            byetext = nyan.new_text(text = 'Your time is out. Your score was: ' + str(score_num), x = 0, y = -150, font_size = 40)
            byetext.show()
            await nyan.sleep(seconds=2)
            retry_button.show()
            menu_button.show()
            retry_button_rect.show()
            menu_button_rect.show()
    
@hole1.when_clicked
async def holeclick1():
    global scorenum_txt
    global score_num
    if hole1.color == 'brown':
        hole1.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@hole2.when_clicked
async def holeclick2():
    global scorenum_txt
    global score_num
    if hole2.color == 'brown':
        hole2.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@hole3.when_clicked
async def holeclick3():
    global scorenum_txt
    global score_num
    if hole3.color == 'brown':
        hole3.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@hole4.when_clicked
async def holeclick4():
    global scorenum_txt
    global score_num
    if hole4.color == 'brown':
        hole4.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@hole5.when_clicked
async def holeclick5():
    global scorenum_txt
    global score_num
    if hole5.color == 'brown':
        hole5.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@hole6.when_clicked
async def holeclick6():
    global scorenum_txt
    global score_num
    if hole6.color == 'brown':
        hole6.color = 'black'
        score_num += 1
        scorenum_txt.text = str(score_num)
    else:
        pass

@start_button.when_clicked
async def startclick():
    global start_button
    global difficulty
    global difficulty_txt
    global difficulty_txt2
    global holes
    global game
    global menu_button
    global gamemode_button_rect
    global gamemode_txt

    start_button.hide()
    start_button_rect.hide()
    menu_button.hide()
    difficulty_txt.hide()
    difficulty_txt2.hide()
    difficulty_rect.hide()
    gamemode_txt.hide()
    gamemode_button_rect.hide()
    catchahole.hide()
    game = True
    while game:
        if gamemode == 'Whackamole':
            holenum = randint(0,5)
            holes[holenum].color = 'brown'
            await nyan.sleep(seconds = difficulty)
            holes[holenum].color = 'black'
        elif gamemode == 'Catchamole':
            for h in holes:
                h.hide()
            catchahole.x = nyan.random_number(-200, 200)
            catchahole.y = nyan.random_number(-200, 200)
            catchahole.show()
            await nyan.sleep(seconds = difficulty)
            catchahole.hide()

@difficulty_txt2.when_clicked
def difclick():
    global difficulty
    global difficulty_txt2
    global difficulty_rect
    if difficulty == 0.8:
        difficulty = 0.6
        difficulty_txt2.text = 'Hard'
        difficulty_rect.color = 'red'
    elif difficulty == 1.0:
        difficulty = 0.8
        difficulty_txt2.text = 'Normal'
        difficulty_rect.color = 'yellow'
    elif difficulty == 0.6:
        difficulty = 1.0
        difficulty_txt2.text = 'Easy'
        difficulty_rect.color = 'green'

@retry_button.when_clicked
async def retclick():
    global byetext
    global score_num
    global scorenum_txt
    global timernum
    global timernumtext
    global game
    global menu_button
    global menu_button_rect

    timernumtext.text = '60'
    timernum = 60
    score_num = 0
    scorenum_txt.text = '0'
    game = True
    retry_button.hide()
    retry_button_rect.hide()
    byetext.hide()
    menu_button.hide()
    menu_button_rect.hide()
    while game:
        holenum = randint(0,5)
        holes[holenum].color = 'brown'
        await nyan.sleep(seconds = difficulty)
        holes[holenum].color = 'black'

@menu_button.when_clicked
async def menuclick():
    global game
    global start_button
    global start_button_rect
    global difficulty_txt
    global difficulty_txt2
    global timernum
    global timernumtext
    global score_num
    global scorenum_txt
    global menu_button
    global byetext
    global retry_button
    global retry_button_rect
    global menu_button_rect
    global difficulty_rect
    global gamemode_button_rect
    global gamemode_txt

    retry_button.hide()
    retry_button_rect.hide()
    menu_button_rect.hide()
    byetext.hide()
    menu_button.hide()
    game = False
    start_button.show()
    start_button_rect.show()
    difficulty_txt.show()
    difficulty_rect.show()
    difficulty_txt2.show()
    gamemode_button_rect.show()
    gamemode_txt.show()
    timernum = 60
    timernumtext.text = '60'
    score_num = 0
    scorenum_txt.text = '0'
    for h in holes:
        h.show()

@gamemode_txt.when_clicked
async def gmdclick():
    global gamemode
    global gamemode_txt
    global hitext
    global holes
    global catchahole
    if gamemode == 'Whackamole':
        gamemode = 'Catchamole'
        hitext.text = 'This is Catch-a-mole!'
        for h in holes:
            h.hide()
        catchahole.x = 0
        catchahole.y = 0
        catchahole.show()
    elif gamemode == 'Catchamole':
        gamemode = 'Whackamole'
        hitext.text = 'This is Whack-a-mole!'
        for h in holes:
            h.show()
        catchahole.hide()
    gamemode_txt.text = str(gamemode)    

@catchahole.when_clicked
async def catchclick():
    global score_num
    global scorenum_txt
    score_num += 1
    scorenum_txt.text = str(score_num)

nyan.start_program()