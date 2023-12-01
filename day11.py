import operator
import math

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

'''
Monkey ops:
1) get current item
2) worry level = (item initial worry level) (op) (increase value)
3) worry level /= 3
4) test(worry level)
5) if test succeeds, run success op; else run fail op
'''

class Monkey:
    def __init__(self, id, item_list, worry_op, divides):
        self.id = id # just for identification purposes
        self.item_list = item_list
        self.worry_op = worry_op
        self.divides = divides
        self.success_monkey = None
        self.fail_monkey = None
        self.num_tosses = 0

    def __str__(self):
        return f'monkey: {self.id}\nitems: {self.item_list}\ndivides: {self.divides}\nsuccess: {self.success_monkey.get_id()}\nfail: {self.fail_monkey.get_id()}\n'
    
    def get_id(self):
        return self.id
    
    def get_num_tosses(self):
        return self.num_tosses
    
    def set_success_monkey(self, success_monkey):
        self.success_monkey = success_monkey

    def set_fail_monkey(self, fail_monkey):
        self.fail_monkey = fail_monkey

    def remove_first_item(self):
        self.item_list = self.item_list[1:]
    
    def receive(self, item):
        self.item_list.append(item)

    def throw_first_item(self, next_monkey):
        next_monkey.receive(self.item_list[0])
        self.remove_first_item()
    
    def decide_which_monkey(self, worry_level):
        if worry_level % self.divides == 0:
            return self.success_monkey
        else:
            return self.fail_monkey

    def inspect_first_item(self):
        self.item_list[0] = math.floor(self.worry_op(self.item_list[0]) / 3)
        next_monkey = self.decide_which_monkey(self.item_list[0])
        self.throw_first_item(next_monkey)
    
    def inspect_all_items(self):
        num_items = len(self.item_list)
        for i in range(num_items):
            self.inspect_first_item()
            self.num_tosses += 1

# format: 'old' * num
def string_to_op(op):
    new_op = op.split(' ')
    if new_op[1] == 'old':
        return lambda x: ops[new_op[0]](x, x)
    return lambda x: ops[new_op[0]](x, int(new_op[1]))

def parse_input():
    with open('day11_input.txt') as f:
        monkey_list = f.read().split('\n\n')
        monkey_list = [monkey.split('\n ')[1:] for monkey in monkey_list]
        monkey_list = [[monkey_op.lstrip().split(': ')[1] for monkey_op in monkey] for monkey in monkey_list]
        refined_monkey_list = []
        for idx, monkey in enumerate(monkey_list):
            item_list, worry_op, divides, success_monkey, fail_monkey = monkey
            item_list = [int(item) for item in item_list.split(', ')]
            worry_op = string_to_op(worry_op[10:])
            divides = int(divides[13:])
            success_monkey = int(success_monkey[16:])
            fail_monkey = int(fail_monkey[16:])
            monkey_list[idx] = [item_list, worry_op, divides, success_monkey, fail_monkey]
            refined_monkey_list.append(Monkey(idx, item_list, worry_op, divides))

        for idx, monkey in enumerate(refined_monkey_list):
            success_monkey, fail_monkey = monkey_list[idx][-2:]
            refined_monkey_list[idx].set_success_monkey(refined_monkey_list[success_monkey])
            refined_monkey_list[idx].set_fail_monkey(refined_monkey_list[fail_monkey])
        return refined_monkey_list

def count_tosses():
    ROUNDS = 20
    monkeys = parse_input()
    highest_toss_count = 0
    second_highest_toss_count = 0
    for i in range(ROUNDS):
        for monkey in monkeys:
            monkey.inspect_all_items()
            if monkey.get_num_tosses() > highest_toss_count:
                second_highest_toss_count = highest_toss_count
                highest_toss_count = monkey.get_num_tosses()
            elif monkey.get_num_tosses() > second_highest_toss_count:
                second_highest_toss_count = monkey.get_num_tosses()
    return highest_toss_count*second_highest_toss_count

print(count_tosses())
