from expyriment import design, control, stimuli
from expyriment.misc import geometry

exp = design.Experiment(name="Labeled Shapes Function")
control.initialize(exp)

SIZE = 50
GAP = 200
OFFSET = GAP // 2 + SIZE // 2


def make_labeled_polygon(n_sides, radius, colour, position, label_text):

    x, y = position

    #polygon
    polygon = stimuli.Shape(
        vertex_list=geometry.vertices_regular_polygon(n_sides, radius),
        colour=colour,
        position=position
    )

    #top of the polygon
    top_y = radius + y

    #line
    line = stimuli.Line(
        start_point=(x, top_y),
        end_point=(x, top_y + 50),
        colour=(255, 255, 255),
        line_width=3
    )

    #label
    label = stimuli.TextLine(
        label_text,
        position=(x, top_y + 70),
        text_colour=(255, 255, 255)
    )

    return [polygon, line, label]


#building triangle with the function
triangle_items = make_labeled_polygon(
    n_sides=3,
    radius=SIZE * 2,
    colour=(128, 0, 128),
    position=(-OFFSET, 0),
    label_text="triangle"
)

#building hexagon
hexagon_items = make_labeled_polygon(
    n_sides=6,
    radius=SIZE,
    colour=(255, 255, 0),
    position=(OFFSET, 0),
    label_text="hexagon"
)

#combine
canvas = stimuli.Canvas(size=exp.screen.size)
for item in triangle_items + hexagon_items:
    item.plot(canvas)

#run
control.start()
canvas.present()
exp.keyboard.wait()
control.end()
