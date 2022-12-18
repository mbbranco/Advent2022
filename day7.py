with open('inputs/test.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

directory_aux = {}
print(lines)
curr_level = 0
directory_dict = {}
directory_files = {}
for l in lines:
    if l[0:5] == "$ cd ":
        directory = l[5:]
        if directory == "..":
            print(f"exiting current dir. entering dir {curr_dir}")
            curr_dir = directory
            curr_level-=1
        else:
            print(f"entering new dir: {directory}")
            curr_dir = directory
            curr_level += 1
            directory_aux[curr_level] = curr_dir
            directory_dict[curr_dir] = curr_level

    else:
        if l.startswith('dir'):
            if curr_dir not in directory_files.keys():
                directory_files[curr_dir] = []
        elif l.startswith('$ ls'):
            continue
        else:
            memory_val = int(l.split(" ")[0])
            if curr_dir in directory_files.keys():
                directory_files[curr_dir].append(memory_val)
            else:
                directory_files[curr_dir] = [memory_val]

print(directory_aux)
print(directory_dict)
print(directory_files)



# directory_mem = {}
# for k_main,val_main in directory_dict.items():
#     total_memory = sum(directory_files[k_main])
#     print(k_main)
#     print(total_memory)
#     for k, val in directory_dict.items():
#         if val_main < val:
#             total_memory += sum(directory_files[k])
#             print(total_memory)
#         else:
#             break
    
#     directory_mem[k_main] = total_memory

# print(directory_mem)

counter = 0
total_sum = 0
for val in directory_mem:
    if val <= 100000:
        counter+=1
        total_sum+=val

print(f'Number of directories with at most 10000: {counter}. Total Sum: {total_sum}')