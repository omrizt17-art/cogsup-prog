from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching")
control.initialize(exp)

SIZE = 50
GAP = 20 #adding the gap
#creating the two squares
red = stimuli.Rectangle(size=(SIZE, SIZE), colour=(255, 0, 0), position=(-400, 0))
green = stimuli.Rectangle(size=(SIZE, SIZE), colour=(0, 255, 0), position=(0, 0))

control.start()

#showing both for 1 sec
canvas = stimuli.Canvas(size=exp.screen.size)
red.plot(canvas)
green.plot(canvas)
canvas.present()
exp.clock.wait(1000)
stop_x = -25 - GAP #testing the noticable gap
#moving the red till he reaches the green
while red.position[0] < stop_x:
    red.move((5, 0))
    canvas = stimuli.Canvas(size=exp.screen.size)
    red.plot(canvas)
    green.plot(canvas)
    canvas.present()
    exp.clock.wait(10) #setting the 'speed' so it'd look like a smooth movement

frames = 0
#now after collision, moving the green
while frames < (400 - 25) // 5:
    green.move((5, 0))
    canvas = stimuli.Canvas(size=exp.screen.size)
    red.plot(canvas)
    green.plot(canvas)
    canvas.present()
    exp.clock.wait(10)
    frames += 1
exp.clock.wait(1000)

control.end()
