from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")
control.initialize(exp)

square = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255))
fixation = stimuli.FixCross()

control.start()

square.present()
fixation.present(clear=False)
exp.clock.wait(500)

square.present(clear=True)
exp.keyboard.wait()

control.end()
