# with open('inputs/text.txt') as f:
#     lines = f.readlines()

# lines = [l.strip() for l in lines]


# folders = {}
# sub_folders = {}
# for l in lines:
#     if '$ cd' in l and l != '$ cd ..':
#         name = l.split(" ")[-1]
#         folders[name] = []
#         sub_folders[name] = []
#         new_dir = True
#     else:
#         if l.split(" ")[0] == 'dir':
#             sub_dir_name = l.split(" ")[-1]
#             folders[name].append(sub_dir_name)
#         else:
#             if l not in ['$ ls','$ cd ..']:
#                 sub_folders[name].append(l)

# print(folders)
# print(sub_folders)

# sub_sizes = {}
# for sub,val in sub_folders.items():
#     size = 0
#     for v in val:
#         size += int(v.split(" ")[0])
#     sub_sizes[sub] = size

# print(sub_sizes)


# sizes = {}
# for dir,sub_f in folders.items():
#     size = 0
#     all_vals = []
#     for f in sub_f:
#         all_vals.append(f)
#         if f in folders.keys():
#             k = folders[f]
#             all_vals.extend(k)
#     print(all_vals)

#     for v in all_vals:
#         size += sub_sizes[f]
#     size += sub_sizes[dir]
#     sizes[dir] = size

# print(sizes)

# # Find all of the directories with a total size of at most 100000. 
# # What is the sum of the total sizes of those directories?
# sum = 0
# for d,s in sizes.items():
#     if s <= 100000:
#         sum+=s
# print(f'Sum of Dir <= 100000: {sum}')

with open('inputs/text.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]


folders = {}
sub_folders = {}
current_dir = lines[0]
main_dir = current_dir
directories_list = []
directories_level = {}
level = -1
directories_files = {}

for l in lines:
    # print(l)
    print(directories_list)
    if l == '$ cd ..':
        print(f'Out! Current Level: {level}')
        level -= 1
        current_dir = directories_list[level]
    elif "$ cd " in l:
        print(l)
        current_dir = l.split(" ")[-1]
        directories_list.append(current_dir)
        level += 1
        directories_level[current_dir] = level
        directories_files[current_dir] = []
    elif "dir" not in l and l!="$ ls":
        mem_val = int(l.split(" ")[0])
        directories_files[current_dir].append(mem_val)

    print(f'Current Dir: {current_dir}')
    print(f'Current Level: {level}')
    print()

print(directories_level)
print(directories_files)

total_memory = {}
for dir_name, level in directories_level.items():
    total_memory[dir_name] =
    