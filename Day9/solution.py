chars = []
file_block = 0 

def find_next_num(characters, index):
    subtraction = 0
    for i in range(len(characters) - index):
        print(characters[i])
        if characters[i] == '.':
            subtraction -= 1
        else: 
            return subtraction
                    


with open('data.txt', 'r') as file:
    line = file.read()
    for i in range(len(line)):
        #odd numbers are files, even numbers can fit things
        if i % 2 == 0:
            for block in range(int(line[i])):
                chars.append(int(file_block))
            file_block += 1
        else:
            for block in range(int(line[i])):
                chars.append('.')

print(chars)

index = 0
right_index = len(chars)-1

file_storage = chars

for char in range(len(file_storage)):
    if file_storage[char] == '.':
        print("location: ", char, "character to insert: ", file_storage[right_index])
        #free space! shove something in it
        if file_storage[char] == '.': 
            #make sure you don't throw another '.' in 
            if file_storage[right_index] == '.':
                right_index = find_next_num(file_storage, right_index)
                file_storage[right_index] = -1
                right_index -= 1
            
            file_storage[char] = file_storage[right_index]
            file_storage[right_index] = -1
            right_index -= 1

print(file_storage)


to_add = []

for file in range(len(file_storage)):
    if not file_storage[file] == -1: 
        to_add.append(file * int (file_storage[file]))

print(sum(to_add))