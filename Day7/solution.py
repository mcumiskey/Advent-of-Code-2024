#import add and mul so I can use them the same way
from operator import add, mul

def solve(target, nums, ops):
    if type(nums) == int:
        #true or false
        return target == nums[1]

    #a and b will be the next two nums evaluated, the rest come along for the ride
    a, b, *rest = nums

    for op in ops:
        if solve(target, [target, op(a, b)] + rest, ops):
            return target
    return 0

dictionary = {}
operators = [add, mul]

with open('data.csv', 'r') as file:
    for line in file:
        #strip the \n character and make array
        string = line.strip()
        #solution occurs before colon
        solution = int(string.split(sep= ':')[0])
        numbers = string.split(sep= ' ')
        for n in range(1, len(numbers)):
            numbers[n] = int(numbers[n])

        dictionary[solution] = numbers[1:]

print(dictionary)

true_lookup = {}

for key in dictionary.keys():
    solve(key, dictionary[key],operators)
    true_lookup[key] = False
    
    if(solve(dictionary[key], key, operators) == 0):
        true_lookup[key] = False
    else:
        true_lookup[key] = True

print(true_lookup)
