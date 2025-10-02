from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE
def present_for(stims, frames):
    if not stims or frames <= 0:
        return
    ms = int(round(frames * (1000/60.0)))  #converting frames to ms
    #drawing the stimuli, clearing first and then presenting all the stimuli
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims)-1))
    exp.clock.wait(ms)

def make_circles(radius, shift=100):
    y = 0
    #setting the positions for the three circles for frame 1
    positions_A = [(-shift, y), (0, y), (shift, y)]
    #setting the positions for the second frame, each circle moves to the right
    positions_B = [(x + shift, y) for x, y in positions_A]
    #creating the circles using the positions for the two frames
    frameA = [stimuli.Circle(radius, position=pos) for pos in positions_A]
    frameB = [stimuli.Circle(radius, position=pos) for pos in positions_B]
    return frameA, frameB

def add_tags(circles, tag_radius=10):
    #setting the color tags for the three circles when called
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for circle, color in zip(circles, colors):
        tag = stimuli.Circle(tag_radius, colour=color, position=(0,0))
        tag.plot(circle)

def run_trial(radius, ISI, with_tags=False):
    #creating the two frames
    frameA, frameB = make_circles(radius)
    #adding the tags if called for
    if with_tags:
        add_tags(frameA)
        add_tags(frameB)
    #preload the circles so that it'll appear faster from memory
    for stim in frameA + frameB:
        stim.preload()

    #running till space is pressed
    while True:
        present_for(frameA, 12) #presenting frameA
        if ISI > 0:
            blank = stimuli.BlankScreen()
            blank.present()
            exp.clock.wait(int(ISI * (1000/60.0))) #setting the time between frame A and frameB according to the ISI
        present_for(frameB, 12)     #presenting frameB

        if exp.keyboard.check(K_SPACE):
            break

if __name__ == "__main__":
    exp = design.Experiment("Ternus illusion")
    control.initialize(exp)

    #low ISI (1 frame)
    run_trial(radius=40, ISI=1, with_tags=False)

    #high ISI (6 frames)
    run_trial(radius=40, ISI=6, with_tags=False)

    #high ISI with tags (6 frames)
    run_trial(radius=40, ISI=6, with_tags=True)

    control.end()
