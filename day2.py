with open('inputs\day2.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

print(lines)

dict_result = {'W':6,'L':0,'D':3}
dict_value = {'X':1,'Y':2,'Z':3}
points_value = 0
points_result = 0
for l in lines:
    you = l[-1]
    elf = l[0]

    if you == 'X':
        if elf == 'A':
            result = 'D'
        elif elf == 'B':
            result = 'L'
        elif elf == 'C':
            result = 'W'

    elif you == 'Y':
        if elf == 'A':
            result = 'W'
        elif elf == 'B':
            result = 'D'
        elif elf == 'C':
            result = 'L'

    elif you == 'Z':
        if elf == 'A':
            result = 'L'
        elif elf == 'B':
            result = 'W'
        elif elf == 'C':
            result = 'D'
    
    points_value += dict_value[you] 
    points_result += dict_result[result]

print(f'Total Result: {points_result}') 
print(f'Total Choice: {points_value}') 
print(f'Total Points Won: {points_result + points_value}') 

print('\nPart 2')

dict_new_key = {'X':'L','Y':'D','Z':'W'}
dict_new_value = {'A':1,'B':2,'C':3}
points_value = 0
points_result = 0
for l in lines:
    you = l[-1]
    elf = l[0]
    result = dict_new_key[you]
    if elf == 'A':
        if you == 'X':
            choice = 'C'
        elif you == 'Y':
            choice = 'A'
        elif you == 'Z':
            choice = 'B'
    elif elf == 'B':
        if you == 'X':
            choice = 'A'
        elif you == 'Y':
            choice = 'B'
        elif you == 'Z':
            choice = 'C'
    elif elf == 'C':
        if you == 'X':
            choice = 'B'
        elif you == 'Y':
            choice = 'C'
        elif you == 'Z':
            choice = 'A'

    points_value += dict_new_value[choice]
    points_result += dict_result[result]

print(f'Total Result: {points_result}') 
print(f'Total Choice: {points_value}') 
print(f'Total Points Won: {points_result + points_value}') 