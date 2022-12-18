with open('inputs/day11.txt') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]
# print(lines)

monkeys = 0
items = []
operations = []
test = []
results = []

#read inputs
for l in lines:
    if 'Monkey' in l:
        monkeys+=1
        res = []
    elif 'Starting items' in l:
        list_items = l.split(": ")[-1]
        list_items = list_items.split(", ")
        list_items = [int(item) for item in list_items]
        items.append(list_items)
    elif 'Operation' in l:
        op = l.split(": ")[-1]
        operations.append(op)
    elif 'Test' in l:
        t = l.split("by ")[-1]
        test.append(int(t))
    elif 'If' in l:
        result = int(l.split(" ")[-1])
        res.append(result)
    else:
        results.append(res)
    
results.append(res)

print(monkeys)
print(items)
print(operations)
print(test)
print(results)

inspections = [0]*monkeys

for r in range(0,20):
    print(f'\nRound {r+1}')
    for m in range(0,monkeys):
        items_m = items[m]
        print(f'\nMonkey {m}')
        print(items_m)
        for item in items_m:
            inspections[m] += 1
            # perform operation
            op_text = operations[m]
            op_text = op_text.split("new = ")[-1]
            op_text = op_text.split(" ")
            op_sign = op_text[1]
            op_right = op_text[2]

            if op_right == 'old':
                op_right = int(item)
            else:
                op_right = int(op_right)

            def calculate_operation(old,new,sign):
                if sign == '+':
                    return old+new
                elif sign == '-':
                    return old-new
                elif sign == "*":
                    return old*new
                else:
                    return old/new
            
            # print(item)
            # print(op_right)
            # print(op_sign)
            print(f'Worry level: {item}')

            op_result = calculate_operation(int(item),op_right,op_sign)
            # print(op_result)
            print(f'New Worry level: {op_result}')
            worry_level = op_result//3
            print(f'Worry level after relief: {worry_level}')
            
            print(f'Worry level divisible by {test[m]}?')

            # test if true or false
            if worry_level % test[m] == 0:
                throw_monkey = results[m][0]
                print('Yes')
            else:
                throw_monkey = results[m][1]
                print('No')
            print(f'Throwing item with worry level of {worry_level} to monkey {throw_monkey}\n')
            items[throw_monkey].append(worry_level)
        
        items[m] = []
        print(items)
    print(f'Round has finished.')

    for m in range(0,monkeys):
        print(f'Monkey {m}: {items[m]}')
    
    max_1 = sorted(inspections,reverse=True)[0]
    max_2 = sorted(inspections,reverse=True)[1]
    monkey_biz = max_1*max_2

    print(f'Total Inspections per Monkey: {inspections}')
    print(f'Total Monkey Business: {monkey_biz}')



