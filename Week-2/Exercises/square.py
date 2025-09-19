from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")
control.initialize(exp)

square = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255))
fixation = stimuli.FixCross()

control.start()

square.present()                      # draw square
fixation.present(clear=False)         # draw fixation on top
exp.clock.wait(500)                   # wait 0.5 sec

square.present(clear=True)            # show only square
exp.keyboard.wait()                   # wait for key press

control.end()
