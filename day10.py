with open('day10.txt') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]
print(lines)


cycle = []
nr_cycles = 0
values = []
cycles_to_check = [20,60,100,140,180,220]
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
        if nr_cycles in cycles_to_check:
            print(f'Sum up to cycle {nr_cycles}: {cycle_sum}')
            cycle.append((int(cycle_sum)+1)*nr_cycles)


print(f'All Cycles: {cycle}')
print(f'Total Sum Cycles: {sum(cycle)}')

        

