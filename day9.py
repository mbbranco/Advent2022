with open('inputs/day9.txt') as f:
    lines = f.readlines()

    
head = [0,0]   
tail = [0,0]
positions_tail = []
for l in lines:
    direction = l.split(" ")[0]
    val = int(l.split(" ")[-1])
    print(l)
    for v in range(0,val):
        if direction == 'U':
            head = [head[0],head[1]+1]
        elif direction == 'D':
            head = [head[0],head[1]-1]
        elif direction == 'R':
            head = [head[0]+1,head[1]]
        elif direction == 'L':
            head = [head[0]-1,head[1]]
        print(f'New Head Position: {head}')
        print(f'Current Tail Position: {tail}')     
        dif_x = head[0]-tail[0]
        dif_y = head[1]-tail[1]
        print(f'Dif x {dif_x} | Dif y {dif_y}')
        if dif_x < 0:
            move_x = dif_x + 1
        else:
            move_x = dif_x - 1

        if dif_y < 0:
            move_y = dif_y + 1
        else:
            move_y = dif_y - 1

        if dif_y in [1,-1] and dif_x in [1,-1]:
            print("ok, touching diagonally")
        elif (dif_x in [0,1,-1] and dif_y == 0) or (dif_y in [0,1,-1] and dif_x == 0):
            print("ok, touching sideways")
        elif dif_x in [2,-2] and dif_y==0:
            print("Move horizontal")
            tail = [tail[0]+move_x,tail[1]]
            print(f'New Tail Position {tail}') 
        elif dif_y in [2,-2] and dif_x==0:
            print("Move vertical")
            tail = [tail[0],tail[1]+move_y]
            print(f'New Tail Position {tail}') 
        elif dif_y in [2,-2] and dif_x in [1,-1]:
            print("Move diagonal and vertical")
            tail = [head[0], tail[1]+move_y]
        elif dif_x in [2,-2] and dif_y in [1,-1]:
            print("Move diagonal and horizontal")
            tail = [tail[0]+move_x, head[1]]
        print(f'Head: {head}. Tail: {tail}\n')     

        positions_tail.append(tail)

unique_pos_tail = []
unique_counter = 0
for p in positions_tail:
    if p not in unique_pos_tail:
        unique_pos_tail.append(p)
        unique_counter +=1

print(f'All Positions Tail: {positions_tail}')
print(f'Unique Positions Tail: {unique_pos_tail}')
print(f'Total Unique Positions Tail: {unique_counter}')