dictionary = {}
from numpy import median

with open('page_orders.csv', 'r') as orders:

    for line in orders:
        #strip the \n character
        string = line.strip()
        nums = string.split(sep= '|')

        if nums[1] not in dictionary:
            dictionary[nums[1]] = []
            dictionary[nums[1]].append(nums[0])
        else: 
            dictionary[nums[1]].append(nums[0])
        
orders.close()

# print (dictionary)

valid_instructions = []
invalid_instructions = []

with open('print_instructions.csv', 'r') as instructions_file:

    for line in instructions_file:
        #strip the \n character and make array
        string = line.strip()

        instructions = string.split(sep= ',')
        
        bad_row = False

        for step in range(len(instructions)-1):
            to_check = instructions[step:]

            if any(i in to_check for i in dictionary[instructions[step]]):
                bad_row = True

        if bad_row is not True:
            valid_instructions.append(instructions)
        else:
            invalid_instructions.append(instructions)

instructions_file.close()

print(valid_instructions)

dumb_sum = 0 
for line in valid_instructions:
    dumb_sum += int(line[int(len(line) / 2)])

print(dumb_sum)

