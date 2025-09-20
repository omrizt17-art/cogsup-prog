from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching Function")
control.initialize(exp)

SIZE = 50


def launching_event(temporal_gap=0, spatial_gap=0, fast_green=False):
    #function gets required parameters

    #reseting squares
    red = stimuli.Rectangle(size=(SIZE, SIZE), colour=(255, 0, 0), position=(-400, 0))
    green = stimuli.Rectangle(size=(SIZE, SIZE), colour=(0, 255, 0), position=(0, 0))

    #showing both for 1 sec
    canvas = stimuli.Canvas(size=exp.screen.size)
    red.plot(canvas)
    green.plot(canvas)
    canvas.present()
    exp.clock.wait(1000)

    #moving red towards green
    stop_x = -25 - spatial_gap
    while red.position[0] < stop_x:
        red.move((5, 0))
        canvas = stimuli.Canvas(size=exp.screen.size)
        red.plot(canvas)
        green.plot(canvas)
        canvas.present()
        exp.clock.wait(10)

    #temporal gap
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)

    #speed green
    if fast_green:
        step = 15  #3x faster
        total_frames = (400 - 25 - spatial_gap) // step
    else:
        step = 5
        total_frames = (400 - 25 - spatial_gap) // step

    frames = 0
    while frames < total_frames:
        green.move((step, 0))
        canvas = stimuli.Canvas(size=exp.screen.size)
        red.plot(canvas)
        green.plot(canvas)
        canvas.present()
        exp.clock.wait(10)
        frames += 1

    #final display
    exp.clock.wait(1000)



control.start()

#michottean launching
launching_event()

# temporal delay (2 sec)
launching_event(temporal_gap=2000)

#spatial gap (40 px)
launching_event(spatial_gap=40)

# triggering (green 3x faster)
launching_event(fast_green=True)

control.end()
