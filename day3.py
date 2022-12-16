import string


with open('inputs\day3.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

print(lines)

abc = list(string.ascii_letters)

priorities = 0
for l in lines:
    nr_items = len(l)
    comp1 = l[:nr_items//2]   
    comp2 = l[nr_items//2:]
    let_comp1 = [c for c in comp1]
    let_comp2 = [c for c in comp2]
    unique_item = set(let_comp1).intersection(set(let_comp2))
    posi = abc.index(list(unique_item)[0])+1
    priorities += posi

print(f'Priorities sum: {priorities}')


priorities = 0
start = 0
for i in range(0,len(lines),3):
    group = lines[i:i+3]
    let_comp1 = [c for c in group[0]]
    let_comp2 = [c for c in group[1]]
    let_comp3 = [c for c in group[2]]
    unique_item = set(let_comp1) & set(let_comp2) & set(let_comp3)
    
    posi = abc.index(list(unique_item)[0])+1
    priorities += posi

print(f'Priorities sum Group: {priorities}')