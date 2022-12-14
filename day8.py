with open('day8.txt') as f:
    lines = f.readlines()

forest = []
for l in lines:
    this_row = [int(ll) for ll in l.strip()]
    forest.append(this_row)

print(forest)

x = len(forest)
y = len(forest[0])
print(f'Size x {x} | y {y}')
vis_counter = (x+y-2)*2
max_score = 0

for i in range(1,y-1):
    for j in range(1,x-1):
        tree = forest[i][j]
        
        tree_up = []
        tree_down = []
        for k in range(0,y):
            if k < i:
                tree_up.append(forest[k][j])
            elif k > i:
                tree_down.append(forest[k][j])

        tree_left = forest[i][:j]
        tree_right = forest[i][j+1:]
        print(tree)
        print(tree_up)
        print(tree_down)
        print(tree_left)
        print(tree_right)

        if max(tree_up) < tree or max(tree_down) < tree or max(tree_left)< tree or max(tree_right)<tree: 
            vis_counter +=1
            print(f'Visible Tree: {tree}')

        def score_view(tree_view,tree):
            score = 0
            for u in tree_view:
                if u < tree:
                    score += 1
                else:
                    score += 1
                    return score

            return score
        
        score_up = score_view(reversed(tree_up),tree)
        score_down = score_view(tree_down,tree)
        score_left = score_view(reversed(tree_left),tree)
        score_right = score_view(tree_right,tree)

        scenic_score = score_up*score_right*score_left*score_down
        print(f'Scenic Score: {scenic_score}')
        if scenic_score>max_score:
            max_score = scenic_score


print(f'Visible: {vis_counter}')
print(f'Max Scenic Score: {max_score}')