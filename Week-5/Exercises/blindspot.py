from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_1, K_2

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """


def make_circle(r, pos=(0, 0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c


""" Experiment """


def run_trial(side="left"):
    #Instructions
    instructions = stimuli.TextScreen(
        "Instructions",
        f"Cover your {side} eye.\n\n"
        "Fixate on the center of the screen.\n\n"
        "Adjust the circle size as instructed.\n\n"
        "When you are ready, press SPACE to start the trial."
    )
    instructions.present()
    exp.keyboard.wait(K_SPACE)
    if side == "left":
        fixation_position = [-300, 0]  #for the left side
    else:
        fixation_position = [300, 0]   #for the right side

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_position)
    fixation.preload()

    radius = 75
    position = [0, 0]  #circle position
    circle = make_circle(radius, pos=position)

    while True:  #staying in the loop till pressing the space
        #drawing the fixation and circle
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)

        key, rt = exp.keyboard.wait(keys=[K_DOWN, K_UP, K_LEFT, K_RIGHT, K_1, K_2, K_SPACE])

        if key == K_SPACE:  #finishing when pressing space
            break
        elif key == K_LEFT:
            position[0] -= 10
        elif key == K_RIGHT:
            position[0] += 10
        elif key == K_UP:
            position[1] += 10
        elif key == K_DOWN:
            position[1] -= 10
        elif key == K_1:  #shrinking the dot
            radius = max(5, radius - 5)
        elif key == K_2:  #growing the dot
            radius += 5

        #updating the circle
        circle = make_circle(radius, pos=position)


control.start(subject_id=1)
run_trial(side="left")
run_trial(side="right")
run_trial()

control.end()
