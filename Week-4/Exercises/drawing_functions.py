from expyriment import design, control, stimuli
import random

def load(stims):
    for stim in stims:
        stim.preload()


def timed_draw(stims):
    t0 = exp.clock.time
    dt = exp.clock.time - t0
    fix_duration = (t0 -dt)/1000
    units = "second" if fix_duration == 1.0 else "seconds"
    duration_text = f"Fixation was present on the screen for {fix_duration} {units}"
    text2 = stimuli.TextLine(duration_text)
    text2.present()
def present_for(stims, t=1000):
    pass


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()