from expyriment import design, control, stimuli
from expyriment.misc import geometry

exp = design.Experiment(name="Labeled Shapes")
control.initialize(exp)

SIZE = 50
GAP = 200
OFFSET = GAP // 2 + SIZE // 2

#shapes
#purple equilateral triangle
triangle = stimuli.Shape(
    vertex_list=geometry.vertices_regular_polygon(3, SIZE * 2),
    colour=(128, 0, 128),
    position=(-OFFSET, 0)
)

#yellow regular hexagon
hexagon = stimuli.Shape(
    vertex_list=geometry.vertices_regular_polygon(6, SIZE),
    colour=(255, 255, 0),
    position=(OFFSET, 0)
)
#lines above shapes
line_triangle = stimuli.Line(
    start_point=(-OFFSET, SIZE),
    end_point=(-OFFSET, SIZE + 50),
    colour=(255, 255, 255),
    line_width=3
)

line_hexagon = stimuli.Line(
    start_point=(OFFSET, SIZE),
    end_point=(OFFSET, SIZE + 50),
    colour=(255, 255, 255),
    line_width=3
)

#labels above lines
label_triangle = stimuli.TextLine(
    "triangle",
    position=(-OFFSET, SIZE + 50 + 20),
    text_colour=(255, 255, 255)
)

label_hexagon = stimuli.TextLine(
    "hexagon",
    position=(OFFSET, SIZE + 50 + 20),
    text_colour=(255, 255, 255)
)

# combine on canvas
canvas = stimuli.Canvas(size=exp.screen.size)
triangle.plot(canvas)
hexagon.plot(canvas)
line_triangle.plot(canvas)
line_hexagon.plot(canvas)
label_triangle.plot(canvas)
label_hexagon.plot(canvas)

# run!
control.start()
canvas.present()
exp.keyboard.wait()
control.end()
