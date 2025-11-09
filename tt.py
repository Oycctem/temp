import re

text = """
Dragons slept across the evergreen.
eagles soared silently over the peaks.
Shadows moved slowly among the echoes.
campfires glimmered near the 123ruins.
lanterns shone faintly across the 0valley.
0ld maps revealed hidden knolls.
_caves echoed softly with crystals.
1mages glowed brightly along the 0ridge.
serpents slithered quietly under the 3stones.
rivers shimmered gently beside the _marsh.
yawning cliffs sheltered small 0nests.
under canopies, creatures _waited.
winds whispered over tall 1solated.
light shimmered across looming looms.
_hidden pathways led to fractured falls.
1llusions glimmered in narrow nooks.
deep within the cave, echoes _rolled.
mountains rose above the 3peaks.
_stones scattered across the 1plain.
night fell silently over _woods.
7hick fog covered the hills.
3rd river ran beneath the _bridge.
whispering leaves danced along hollow.
1lluminated lanterns guided the 7h.
3mall streams glistened beneath _arces.
shrubs swayed near the pebbles.
4ootprints led across cliff.
3ld oak trees marked secret spaces.
_moss covered the hidden boulder.
3ddies of water spun past twisting .
whisps of fog lingered near 3rocks.
3arth trembled slightly beneath northern.
125 nsects hummed softly through 2imeless nights.
"""

def extract_flag(text):
    flag_letters = []
    lines = text.splitlines()
    for line in lines:
        # Match number followed by letters
        num_match = re.search(r'(\d+)([a-zA-Z]+)', line)
        if num_match:
            num, word = num_match.groups()
            index = int(num) - 1  # treat as 1-indexed
            if index < len(word):
                flag_letters.append(word[index])
            continue
        # Match underscore followed by word
        underscore_match = re.search(r'_([a-zA-Z]+)', line)
        if underscore_match:
            flag_letters.append(underscore_match.group(1)[0])
            continue
    return ''.join(flag_letters)

flag = extract_flag(text)
print("Flag letters:", flag)
