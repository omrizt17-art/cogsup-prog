from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE
#control.set_develop_mode(True)
exp = design.Experiment(
    name="Kanizsa Rectangle",
    background_colour=C_GREY
)
def kanizsa_rectangle(r_aspect_ratio, r_scaling, c_scaling):
    control.initialize(exp)
    screen_w, screen_h = exp.screen.size
    rectangle_height = r_scaling * screen_h #illusory rectangle
    rectangle_width = rectangle_height / r_aspect_ratio
    radius= c_scaling * screen_w  #circle radius
    offset_x = rectangle_width / 2 #distance from screen center to rectangle edges
    offset_y = rectangle_height / 2

    canvas = stimuli.Canvas(size=exp.screen.size)

    #defining a function to draw the 'pacman'
    def draw_pacman(center_xy, colour, cut_dx, cut_dy, ):
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
    draw_pacman(center_xy=(-offset_x,  offset_y), colour=C_BLACK, cut_dx=+radius/2, cut_dy=-radius/2)  #top left
    draw_pacman(center_xy=(+offset_x,  offset_y), colour=C_BLACK, cut_dx=-radius/2, cut_dy=-radius/2)  #top right
    draw_pacman(center_xy=(-offset_x, -offset_y), colour=C_WHITE, cut_dx=+radius/2, cut_dy=+radius/2)  #bottom left
    draw_pacman(center_xy=(+offset_x, -offset_y), colour=C_WHITE, cut_dx=-radius/2, cut_dy=+radius/2)  #bottom right
    canvas.present()
    exp.keyboard.wait()
kanizsa_rectangle(r_aspect_ratio=2.0, r_scaling=0.5, c_scaling=0.05)