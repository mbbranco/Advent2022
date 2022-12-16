with open('inputs/day5.txt') as f:
    lines = f.readlines()

mode = 'part2'

movements = []
pyramid = []
for l in lines:

    if l[0]=='m':
        movements.append(l.strip())
    else:
        if l[0:3] != ' 1 ' and l != '\n':
            pyramid.append(l)

stacks = []
positions = list(range(1,len(pyramid[0]),4))
print(pyramid)
for p in positions:
    pyr = []
    for row in pyramid:
        if row[p] != ' ':
            pyr.append(row[p])
    stacks.append(pyr)

print(stacks)

for m in movements:
    print(m)
    nr_pops = int(m.split('move ')[-1].split(' from')[0])
    from_pos = int(m.split('from ')[-1].split(' to')[0])-1
    to_pos = int(m.split('to ')[-1])-1
    
    values_popped = stacks[from_pos][0:nr_pops]
    print(f'Values Popped: {values_popped}')
    if mode == 'part2':
        values_popped = reversed(values_popped)

    for v in values_popped:
        stacks[from_pos].pop(0)
        stacks[to_pos].insert(0,v)
    print(f'Final Stack: {stacks}')

print()
final = ''
for s in stacks:
    final += s[0]
print(f'Top stacked values: {final}')

