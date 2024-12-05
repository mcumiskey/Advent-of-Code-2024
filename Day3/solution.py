import re

#Part 1 
f = open('data.txt', 'r')
content = f.read()
f.close()

# print(content)
muls = re.findall(r"mul\(\d+,\d+\)", content) 

multiplied = []

for nums in muls:
    to_multiply = []
    x = [s for s in nums.split(',')]
    for piece in x:
        number = re.findall(r'[\d]+', piece)
        to_multiply.append(int(number[0]))
    
    multiplied.append(to_multiply[0] * to_multiply [1])
    # print(to_multiply)

print(sum(multiplied))
        
        
