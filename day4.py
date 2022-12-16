with open('inputs/day4.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

elf1 = []
elf2 = []
contains = 0
intersects = 0
for l in lines:
    l1,l2 = l.split(",")
    min_l1,max_l1 = l1.split("-")
    min_l2,max_l2 = l2.split("-")
    min_l1 = int(min_l1)
    max_l1 = int(max_l1)
    min_l2 = int(min_l2)
    max_l2 = int(max_l2)

    if (min_l1 <= max_l2 and min_l1 >= min_l2) and (max_l1 <= max_l2 and max_l1 >= min_l2):
        contains+=1
    elif (min_l2 <= max_l1 and min_l2 >= min_l1) and (max_l2 <= max_l1 and max_l2 >= min_l1):
        contains+=1

    l1_range = range(min_l1,max_l1+1)
    l2_range = range(min_l2,max_l2+1)

    if set(l1_range) & set(l2_range):
        intersects +=1
 

print(f'Contained: {contains}')
print(f'Intersected: {intersects}')
