with open('inputs/test2.txt') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]
print(lines)


cycle = []
nr_cycles = 0
values = []
cycles_to_check = [20,60,100,140,180,220]
sprite_position = [] 
for i,op in enumerate(lines):
    operation = op[0:4]
    if operation == 'noop':
        loop_nr = 1
    else:
        value = op[5:]
        loop_nr = 2

    values.append(int(value))

    for k in range(0,loop_nr):
        nr_cycles+=1
        cycle_sum = sum(values[0:i])
        sprite_position.append(int(cycle_sum)+1)
        
        if nr_cycles in cycles_to_check:
            print(f'Sum up to cycle {nr_cycles}: {cycle_sum}')
            cycle.append((int(cycle_sum)+1)*nr_cycles)


print(f'All Cycles: {cycle}')
print(f'Total Sum Cycles: {sum(cycle)}')


print("\nPart 2")
cycles_to_break = [40*i for i in range(1,7)]

sprite = ["#","#","#"]
sprite.extend(["."]*36)
initial_sprite = sprite.copy()

current_crt_row = []
print(sprite_position)
crts = []
for i,p in enumerate(sprite_position):
    if i in cycles_to_check:
        crts.append(current_crt_row)
        current_crt_row = []
        print('Reset CRT\n')

    print(f'Cycle {i} - Position Start {p}')
    print(F'Sprite: {sprite}')
    
    sprite = ["."] * 39
    for k in range(p-1,p-1+3):
        sprite[k] = "#"

    sprite_pos = sprite[i]
    if sprite_pos == "#":
        current_crt_row.append("#")
    else:
        current_crt_row.append(".")
    print(f'Current CRT: {current_crt_row}')

print(crts)


