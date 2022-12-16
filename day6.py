with open('inputs/text.txt') as f:
    lines = f.readlines()

mode = 'part2'
if mode == 'part1':
    signal_len = 4
else:
    signal_len = 14

for l in lines:
    for i in range(0,len(l)-signal_len):
        sub_sec = l[i:i+signal_len]
        print(sub_sec)
        signal_found = True
        for s in sub_sec:
            if sub_sec.count(s)>1:
                signal_found = False
                break
        if signal_found:
            print(f'Mode: {mode}. Signal Found! Position {i+signal_len}')
            break

