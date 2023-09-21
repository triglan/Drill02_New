from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(5)

def run_circle():
    print('Circle')
    pass

def run_rectangle():
    print('Rectangle')
    pass
    


while True:
    run_circle()
    run_rectangle()

close_canvas()

