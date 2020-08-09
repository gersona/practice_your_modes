import sys, random, getopt

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
        sys.stderr.write("the Key "+ key + "doesn't exist")
        sys.exit(1)

def major_mode(key, mode_val):
    # scales are 1-indexed, python is 0-indexed
    mode_val = mode_val - 1 
    if mode_val == 0:
        root  = key
    else:
        key_idx = keys.index(key)
        root_idx = int(key_idx + (sum(major_scale_tones[:mode_val])) * 2)
        root = keys[root_idx]
    tones = major_scale_tones[mode_val:] + major_scale_tones[:mode_val]
    return get_scale(tones, root)


if __name__ == "__main__":
    key, mode_name, mode_value = None, None, None
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "hk:m:", ["help", "key=", "mode="])
    except getopt.GetoptError:
        sys.stderr.write("Some error with the option args")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("I can't help you for now")

        if opt in ("-k", "--key"):
            key = arg.upper()
            if key not in keys:
                sys.stderr.write(f"{key} is an unknown key")
                sys.exit(1)

        if opt in ("-m", "--mode"):
            try:
                mode_value = int(arg)
                if mode_value not in range(1, 7):
                    raise Exception
                mode_name = modes[mode_value - 1][0]
            except (TypeError, Exception):
                mode_name = arg.upper()
                match = [m[1] for m in modes if m[0] == mode_name]
                if match:
                    mode_value = match[1]
                else:
                    mode_names = [m[0] for m in modes]
                    mode_values = [m[1] for m in modes]
                    sys.stderr.write(f"{arg} is isn't a valid mode value \n")
                    sys.stderr.write(f"Accepted input any value in {mode_names} ")
                    sys.stderr.write(f"or {mode_values} \n")
                    sys.exit(1)

    if mode_name is None:
        mode_name, mode_value = random.choice(modes)
    if key is None:
        key = random.choice(keys)

    mode = major_mode(key, mode_value)
    print(f"Major {mode_name} mode of {key} (start @ {mode_value})")
    answer = input("Type the keys (separated by a blank)")
    answer = answer.split(' ')
    if mode == answer:
        print("CORRECT!")
    else:
        print("Correct answer is")
        print(" - ".join(mode))
