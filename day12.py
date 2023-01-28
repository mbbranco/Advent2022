import string


with open('inputs/test.txt') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]
print(lines)


i=0
for i,l in enumerate(lines):
    aux = []
    j = 0
    for a in l:
        if a == 'S':
            start_pos = [i,j]
        if a =='E':
            end_pos = [i,j]
        j+=1

lowercase = string.ascii_lowercase

nr_steps = 0
end_not_found = False
last_move = ''
while not end_not_found:
    cur_val = lines[start_pos[0]][start_pos[1]]
    print(cur_val)
    if cur_val == 'E':
        end_not_found = True
    if cur_val == 'S':
        cur_val = 'a'

    difs = {}

    def check_pos(cur_val,other_val):
        cur_val_i = lowercase.find(cur_val)
        other_val_i = lowercase.find(other_val)
        print(cur_val_i)
        print(other_val_i)
        return other_val_i-cur_val_i

    # check pos left
    if start_pos[1]-1 > 0 and last_move!='L':
        left_val = lines[start_pos[0]][start_pos[1]-1]
        dif = check_pos(cur_val,left_val)
        difs['L'] = dif

    # check pos right
    if start_pos[1]+1 < len(lines[start_pos[0]]) and last_move!='R':
        right_val = lines[start_pos[0]][start_pos[1]+1]
        print(right_val)
        dif = check_pos(cur_val,right_val)
        difs['R'] = dif

    # check pos up
    if start_pos[0]-1>0 and last_move!='U':
        up_val = lines[start_pos[0]-1][start_pos[1]]
        print(up_val)
        dif = check_pos(cur_val,up_val)
        difs['U'] = dif
        
    # check pos down
    if start_pos[0]+1<len(lines) and last_move!='D':
        down_val = lines[start_pos[0]+1][start_pos[1]]
        print(down_val)
        dif = check_pos(cur_val,down_val)
        difs['D'] = dif

    def call_move(move_type,start_pos):
        if move_type == 'D':
            print('move down')
            start_pos = [start_pos[0]+1,start_pos[1]]
            last_move = 'D'
        elif move_type == 'U':
            print('move UP')
            start_pos = [start_pos[0]-1,start_pos[1]]
            last_move = 'U'
        elif move_type == 'R':
            print('move right')
            start_pos = [start_pos[0],start_pos[1]+1]
            last_move = 'R'
        elif move_type == 'L':
            print('move left')
            start_pos = [start_pos[0],start_pos[1]-1]
            last_move = 'L'
        
        return start_pos,last_move

    ok = False
    for move,dif in difs.items():
        if dif == 1:
            print(f'Move {move}')
            start_pos,last_move = call_move(move,start_pos)
            ok = True
            break

    if not ok:
        for move,dif in difs.items():
            if dif == 0:
                print(f'Move {move}')
                start_pos,last_move = call_move(move,start_pos)
                ok = True
                break 

    nr_steps+=1


print(nr_steps)

