with open('inputs\day1.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

elf = []
sum_l = 0
max_l = 0
for l in lines:
    if l == "":
        if sum_l >= max_l:
            max_l = sum_l
        elf.append(sum_l)
        sum_l = 0
    else:
        sum_l += int(l)

print(f'Maximum Elf: {max_l}')

elf = sorted(elf,reverse=True)
print(f'Top 3 Elfs: {elf[0:3]}')
print(f'Sum Top 3 Elfs: {sum(elf[0:3])}')