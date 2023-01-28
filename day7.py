with open('inputs/test.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

print(lines)
directories = []
memories = {}
memory = 0
level = -1
for l in lines:
    if l[0:5] == "$ cd ":
        directory = l[5:]
        if directory == "..":
            level-=1
            print(f"exiting current dir. entering dir {directories[level]}")
            curr_dir = directories[level]
        else:
            print(f"entering new dir: {directory}")
            memory = 0
            directories.append(directory)
            curr_dir = directory
            level+=1

    else:
        if l.startswith('dir') or l.startswith('$ ls'):
            continue
        else:
            memory_val = int(l.split(" ")[0])
            memory+=memory_val
            for d in directories[:level]:
                memories[d]+=memory_val
            
            memories[directory] = memory



    print(memories)

counter = 0
total_sum = 0
for k,val in memories.items():
    if val <= 100000:
        counter+=1
        total_sum+=val

print(f'Number of directories with at most 10000: {counter}. Total Sum: {total_sum}')