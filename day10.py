with open('inputs/DAY10.txt') as f:
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
        value = 0
        loop_nr = 1
    else:
        value = op[5:]
        loop_nr = 2

    values.append(int(value))

    for k in range(0,loop_nr):
        nr_cycles+=1
        cycle_sum = sum(values[0:i])
        sprite_position.append(cycle_sum+1)
        
        if nr_cycles in cycles_to_check:
            print(f'Sum up to cycle {nr_cycles}: {cycle_sum}')
            cycle.append((int(cycle_sum)+1)*nr_cycles)


print(f'All Cycles: {cycle}')
print(f'Total Sum Cycles: {sum(cycle)}')


print("\nPart 2")

sprites = []
current_sprite = ["#","#","#"]
current_sprite.extend(["."]*36)
sprites.append(current_sprite)
sprites.extend([["."]*39]*5)

crts=[]
current_crt_row = []
print(sprite_position)
crts = [["."]*39]*6

print(sprites)
print(crts)
for i,p in enumerate(sprite_position):
    print(f'Cycle {i} - Position Start {p}')
    current_crt_row = crts[i//39]
    current_sprite = sprites[p//40]
    print(f'Current CRT: {current_crt_row}')
    
    p = p-(p//40)*40

    current_sprite = ["."] * 39
    for k in range(p-1,p-1+3):
        current_sprite[k] = "#"
    print(F'     Sprite: {current_sprite}')

    sprites[p//40] = current_sprite

    sprite_pos = current_sprite[i-(i//39)*39]
    if sprite_pos == "#":
        current_crt_row[i-(i//39)*39] = "#"
    else:
        current_crt_row[i-(i//39)*39] = "."

    crts[i//39] = current_crt_row
    print(f'  Final CRT: {current_crt_row}')



