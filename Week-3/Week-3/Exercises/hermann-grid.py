
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE, C_GREY

def hermann_grid(square_size, square_color, space, rows, cols, bg_color):
    #control.set_develop_mode(True)
    exp = design.Experiment(
        name="Hermann Grid",
        background_colour=bg_color
    )
    control.initialize(exp)
    canvas = stimuli.Canvas(size=exp.screen.size)
    #height and width of all squares and width of all gaps
    grid_w = cols*square_size + (cols - 1)*space #width of all squares and width of all gaps
    grid_h = rows * square_size + (rows - 1) * space
    #top left corner offset
    start_x = -grid_w/2 + square_size/2
    start_y = +grid_h/2 - square_size/2
    #running over the height and width of the grid
    for i in range(rows):
        for j in range(cols):
            cx = start_x + j*(square_size + space)
            cy = start_y -i*(square_size + space)
            sq = stimuli.Rectangle(size=(square_size, square_size),
                                   colour=square_color)
            sq.reposition((cx, cy))
            sq.plot(canvas)
    canvas.present()
    exp.keyboard.wait()
hermann_grid(square_size=200,square_color=C_BLACK,space=15,rows=3,cols=3,
                 bg_color=C_WHITE)
