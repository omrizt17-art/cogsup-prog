from expyriment import design, control, stimuli
exp = design.Experiment(name="display edges")
control.set_develop_mode()
control.initialize(exp)
#setting the experiment
width, height = exp.screen.size
print(width, height)
size_square = int(0.05 * width)
red = (255, 0, 0)
top_left_position     = (-width//2 + size_square//2,  height//2 - size_square//2)
top_right_position    = ( width//2 - size_square//2,  height//2 - size_square//2)
bottom_left_position  = (-width//2 + size_square//2, -height//2 + size_square//2)
bottom_right_position = ( width//2 - size_square//2, -height//2 + size_square//2)
top_left_square = stimuli.Rectangle(size=(size_square, size_square),
                                    position=top_left_position,
                                    colour=(255, 0, 0),
                                    line_width=1)

top_right_square = stimuli.Rectangle(size=(size_square, size_square),
                                     position=top_right_position,
                                     colour=(255, 0, 0),
                                     line_width=1)

bottom_right_square = stimuli.Rectangle(size=(size_square, size_square),
                                        position=bottom_right_position,
                                        colour=(255, 0, 0),
                                        line_width=1)

bottom_left_square = stimuli.Rectangle(size=(size_square, size_square),
                                       position=bottom_left_position,
                                       colour=(255, 0, 0),
                                       line_width=1)


#running experiment
#control.start()
canvas = stimuli.Canvas(size=exp.screen.size)
top_left_square.plot(canvas)
top_right_square.plot(canvas)
bottom_left_square.plot(canvas)
bottom_right_square.plot(canvas)
canvas.present()
exp.keyboard.wait()
control.end()