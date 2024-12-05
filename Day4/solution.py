lines = []
coords = []

def validate_xmas(x, y, vx=0,vy=0):
    '''
    using the velocity (positive or negative, 8 directions) first check if a substring will be in bounds 
    if it is in bounds, then grab the next three characters in that direction and check if it equals xmas 
    '''
    # if the x position is too close to the left or right so that the string would be less than 4 characters (and therefore not xmas) return false
    if(x + (vx * 3)) < 0 or (x+ (vx * 3)) >= len(lines[0]):
        return False
    # if the y position is too close to the top or bottom so that the string would be less than 4 characters (and therefore not xmas) return false
    if(y + (vy * 3)) < 0 or (y + (vy * 3)) >= len(lines): 
        return False
    
    substring = lines[x + (vx * 0)][y + (vy * 0)] + \
                lines[x + (vx * 1)][y + (vy * 1)] + \
                lines[x + (vx * 2)][y + (vy * 2)] + \
                lines[x + (vx * 3)][y + (vy * 3)]
    
    if substring == 'XMAS':
        return True
    else:
        return False
    

with open('data.csv', 'r') as file:
    #manually keep track of row being read
    row = 0

    for line in file:
        #strip the \n character and make char array
        letters = list(line.strip())
        lines.append(letters)

        for i in range(len(letters)):
            #xmas has to start with X
            if letters[i] == 'X':
                #append a tuple to the 1d array 
                coords.append((row, i))

        #manually keep track of row
        row += 1

file.close()

total_xmas = 0

for i in coords:
    x_pos = i[0]
    y_pos = i[1]

    for vx in [-1, 0, 1]:
        for vy in [-1, 0, 1]:
            #the combos of [-1][-1], [-1][0], [0][-1]..... make up the 8 search directions 
            if validate_xmas(x_pos, y_pos, vx, vy):
                total_xmas += 1

print(total_xmas)

    