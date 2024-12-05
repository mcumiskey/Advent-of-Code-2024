import pandas as pd

data = pd.read_csv('data.csv', sep= r'\s+', names= ['row1', 'row2'])

row_1 = data['row1'].to_list()
row_2 = data['row2'].to_list()

row_1.sort()
row_2.sort()

distances = []

for i in range(len(row_1)):
    distances.append(abs(row_1[i] - row_2[i]))

print(sum(distances))