with open('test.txt') as f:
    lines = f.readlines()



def check_pos(x_head,y_head,x_tail,y_tail):
    if abs(x_head-x_tail) == 1 and abs(y_head-y_tail) == 1:
        return 0
    elif abs(x_head-x_tail) == 2 or abs(y_head-y_tail) == 2:
        return 2
    else:
        return 1

x_head,y_head = 0,0
x_tail,y_tail = -1,-1
tail_positions = []
for l in lines:
    direction = l.split(" ")[0]
    val = int(l.split(" ")[-1])
    print(l)
    print(x_head,y_head)
    print(x_tail,y_tail)
    print()

    for v in range(1,val+1):
        if direction == 'U':
            y_head += 1
            cp = check_pos(x_head,y_head,x_tail,y_tail)
            if cp == 1:
                y_tail+=1
            elif cp == 2:
                x_tail = x_head
                y_tail = y_head-1

        elif direction == 'D':
            y_head -= 1
            cp = check_pos(x_head,y_head,x_tail,y_tail)
            if cp == 1:
                y_tail-=1
            elif cp == 2:
                x_tail = x_head
                y_tail = y_head+1

        elif direction == 'L':
            x_head -= 1
            cp = check_pos(x_head,y_head,x_tail,y_tail)
            if cp == 1:
                x_tail-=1
            elif cp == 2:
                x_tail = x_head+1
                y_tail = y_head
                
        elif direction == 'R':
            x_head += 1
            cp = check_pos(x_head,y_head,x_tail,y_tail)
            if cp == 1:
                x_tail+=1
            elif cp == 2:
                x_tail = x_head-1
                y_tail = y_head
                
        tail_pos = (x_tail,y_tail)
        head_pos = (x_head,y_head)
        if tail_pos not in tail_positions:
            tail_positions.append(tail_pos)
        print()
        print(head_pos)
        print(tail_pos)
print(f'Number of diff tail positions: {len(tail_positions)}')
print(tail_positions)