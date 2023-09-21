from pico2d import *
import math
open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(1)

def run_circle():
    print('Circle')
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.02)
    

def run_rectangle():
    print('Rectangle')
    
    # bottom line
    for x in range(50, 750+1, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.02)
        
   
    


while True:
    #   run_circle()
    run_rectangle()
    break

close_canvas()

