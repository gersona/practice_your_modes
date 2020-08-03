import sys
import random

modes = [
    ('IONIAN', 1), ('DORIAN', 2), ('PHRYGIAN', 3), ('LYDIAN', 4),
    ('MYXOLIDIAN', 5), ('AEOLIAN', 6), ('LOCRIAN', 7)
]

keys = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']
major_scale_tones = [1, 1, 0.5, 1, 1, 1, 0.5]

def get_scale(tones, key):
    index = keys.index(key)
    scale = [key]
    for tone in tones:
        index = (index +  int(tone * 2)) % len(keys) 
        scale.append(keys[index])
    return scale

def major_scale(key):
    if key in keys:
        return get_scale(major_scale_tones, key)
    else:
        sys.stderr("the Key "+ key + "doesn't exist")
        sys.exit(1)

def major_mode(key, mode):
    key_idx = keys.index(key)
    root = keys[int(key_idx + (major_scale_tones[mode] * 2))]
    tones = major_scale_tones[mode:] + major_scale_tones[:mode]
    print(root, tones)
    return get_scale(tones, root)

if __name__ == "__main__":
    key = random.choice(keys)
    mode_name, mode_value = random.choice(modes)
    scale = major_scale(key)
    mode = major_mode(key, mode_value - 1)
    print(f"Major {mode_name} mode of {key}")
    print(mode)
