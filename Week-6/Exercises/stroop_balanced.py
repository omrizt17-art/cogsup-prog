from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
import random, itertools

# === CONSTANTS ===
COLORS = ["red", "blue", "green", "orange"]
COLOR_MAP = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 200, 0),
    "orange": (255, 165, 0)
}
N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16
#what the subject should press 
KEYMAP = {
    "red": "f",
    "blue": "g",
    "green": "h",
    "orange": "j"
}

def derangements(lst): #creating the derangements function that will make sure no color stays in its place
    ders = []
    for perm in itertools.permutations(lst):
        if all(a != b for a, b in zip(lst, perm)):
            ders.append(perm)
    return ders

def load(stims):
    for s in stims: s.preload()

def present_for(*stims, t=1000):
    t0 = exp.clock.time
    exp.screen.clear()
    for s in stims:
        s.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(t - (exp.clock.time - t0))

# === EXPERIMENT SETUP ===
exp = design.Experiment(name="Balanced Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["block", "trial", "trial_type", "word", "color", "RT", "correct"])

control.set_develop_mode()
control.initialize(exp)

fix = stimuli.FixCross()
fix.preload()

# === TRIAL CREATION ===
PERMS = derangements(COLORS)
subject_id = 1
perm = PERMS[(subject_id - 1) % len(PERMS)]

base_trials = (
    [{"trial_type": "match", "word": c, "color": c} for c in COLORS] +
    [{"trial_type": "mismatch", "word": w, "color": c} for w, c in zip(COLORS, perm)]
)

# === CREATE BLOCKS ===
blocks = []
reps = N_TRIALS_IN_BLOCK // len(base_trials)
for b in range(1, N_BLOCKS + 1):
    b_trials = base_trials * reps
    random.shuffle(b_trials)
    blocks.append(b_trials)

# === RUN ===
control.start(subject_id=subject_id)

instr = stimuli.TextScreen("Instructions",
    "Name the COLOR of the word on screen.\n\n"
    "Press:\nF = Red\nG = Blue\nH = Green\nJ = Orange\n\nPress SPACE to start.")
instr.present()
exp.keyboard.wait()

for b, trials in enumerate(blocks, 1):
    for t, trial in enumerate(trials, 1):
        word, color, ttype = trial["word"], trial["color"], trial["trial_type"]
        stim = stimuli.TextLine(word, text_colour=COLOR_MAP[color])
        fix.present()
        exp.clock.wait(500)
        stim.present()
        key, rt = exp.keyboard.wait([ord(k) for k in KEYMAP.values()])
        correct = key == ord(KEYMAP[color])
        exp.data.add([b, t, ttype, word, color, rt, correct])
        feedback = stimuli.TextLine("Correct!" if correct else "Incorrect!")
        present_for(feedback, t=700)
    if b != N_BLOCKS:
        stimuli.TextScreen("Break", "Take a short break.\nPress SPACE to continue.").present()
        exp.keyboard.wait()

stimuli.TextScreen("End", "Well done!").present()
exp.keyboard.wait()
control.end()
