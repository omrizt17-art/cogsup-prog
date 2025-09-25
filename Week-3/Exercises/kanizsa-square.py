from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE
#control.set_develop_mode(True)
exp = design.Experiment(
    name="Kanizsa Square",
    background_colour=C_GREY
)
control.initialize(exp)
screen_w, screen_h = exp.screen.size
square_side = int(0.25 * screen_w)   #illusory square
radius= int(0.05 * screen_w)   #circle radius
offset= square_side / 2        #distance from screen center to each circle center

canvas = stimuli.Canvas(size=exp.screen.size)

#defining a function to draw the 'pacman'
def draw_pacman(center_xy, colour, cut_dx, cut_dy):
    """Draw a Pac-Man (circle + square 'mouth') at center_xy."""
    #designing the circle
    circle = stimuli.Circle(radius=radius, colour=colour, anti_aliasing=8)
    circle.reposition(center_xy)
    circle.plot(canvas)

    #designing the 'mouth' of pacman
    cut = stimuli.Rectangle(size=(radius, radius), colour=C_GREY) #rectangle that has the sma ecolor as the background
    cx, cy = center_xy #the center of the triangle
    cut.reposition((cx + cut_dx, cy + cut_dy)) #tart from cx and go cut_dx horizontally, start from cy and go cut_dy vertically
    cut.plot(canvas)

#calling the functions for the 4 pacmans
draw_pacman(center_xy=(-offset,  offset), colour=C_BLACK, cut_dx=+radius/2, cut_dy=-radius/2)  #top left
draw_pacman(center_xy=(+offset,  offset), colour=C_BLACK, cut_dx=-radius/2, cut_dy=-radius/2)  #top right
draw_pacman(center_xy=(-offset, -offset), colour=C_WHITE, cut_dx=+radius/2, cut_dy=+radius/2)  #bottom left
draw_pacman(center_xy=(+offset, -offset), colour=C_WHITE, cut_dx=-radius/2, cut_dy=+radius/2)  #bottom right
canvas.present()
exp.keyboard.wait()
