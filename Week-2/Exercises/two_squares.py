from expyriment import design, control, stimuli

exp = design.Experiment(name="Two Squares")
control.initialize(exp)

SIZE = 50
GAP = 200
OFFSET = GAP // 2 + SIZE // 2


left_sq  = stimuli.Rectangle(size=(SIZE, SIZE), colour=(255, 0, 0), position=(-OFFSET, 0))
right_sq = stimuli.Rectangle(size=(SIZE, SIZE), colour=(0, 255, 0), position=( OFFSET, 0))


canvas = stimuli.Canvas(size=exp.screen.size)
left_sq.plot(canvas)
right_sq.plot(canvas)

control.start()
canvas.present()
exp.keyboard.wait()
control.end()
