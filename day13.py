import ast
with open('inputs/test.txt') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]
print(lines)

nr_lines = len(lines)
nr_pairs = nr_lines//2

pairs = []
for i in range(0,nr_pairs,3):
    pairs.append(lines[i:i+2])

print(pairs)


def compare_lists(l1,l2):
    for i,l in enumerate(l1):
        if l2[i] > l1[i]:
            return False
    return True

def compare_numbers(n1,n2):
    if n1>n2:
        return False
    else:
        return True

order = []
for p in pairs:
    list_1 = ast.literal_eval(p[0])
    list_2 = ast.literal_eval(p[1])
    print(f'Pair: {list_1} || {list_2}')
    pair_wrong = False
    for i,l in enumerate(list_1):
        print(l)
        if type(list_1[i]) == type(list_2[i]) == int:
            print('Comparing Integers')
            eval = compare_numbers(list_1[i],list_2[i])
            if eval == False:
                pair_wrong = True
                break
            else:
                pair_wrong = False
        
        elif type(list_1[i]) == type(list_2[i]) == list:
            print('Comparing Lists')

            for j,l in enumerate(list_1[i]):
                    if type(list_1[i][j]) == type(list_2[i][j]) == int:
                        print('Comparing Integers inside list')
                        wrong = compare_numbers(list_1[i][j],list_2[i][j])
                        if wrong == False:
                            pair_wrong = True
                            break
                        else:
                            pair_wrong = False

        elif type(list_1[i]) != type(list_2[i]):
            print('Comparing Mixed Types')
            if type(list_2[i]) == int:
                list_2 = list(list_2[i])
            elif type(list_1[i]) == int:
                list_1 = list(list_1[i])

                for j,l in enumerate(list_1[i]):
                        if type(list_1[i][j]) == type(list_2[i][j]) == int:
                            print('Comparing Integers inside list with mixed types')
                            wrong = compare_numbers(list_1[i][j],list_2[i][j])
                            if wrong == False:
                                pair_wrong = True
                                break
                            else:
                                pair_wrong = False

        else:
            print('?')
        
        print(f'Status: {pair_wrong}')
    print(f'Final Status Pair: {pair_wrong}\n')