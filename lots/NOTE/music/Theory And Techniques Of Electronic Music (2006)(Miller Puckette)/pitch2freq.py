
'''
MIDI
    pitch[69] = 440Hz
    pitch[60] = middle C
'''
def pitch2freq__MIDI(pitch):
    return 440* 2**((pitch-69)/12)

assert pitch2freq__MIDI(69) == 440
assert pitch2freq__MIDI(69+12) == 880


