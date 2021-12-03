my_input = open('input.txt').read().split('\n')
my_data = []
horz = 0
depth = 0
aim = 0

for i in range(len(my_input)):
    my_data.append(tuple(my_input[i].split()))
    my_data[i] = str (my_data[i][0]), int (my_data[i][1])

for k in range(len(my_data)):
    if my_data[k][0] == 'forward':
        horz += my_data[k][1]
        depth += aim * my_data[k][1]
    if my_data[k][0] == 'up': aim -= my_data[k][1]
    if my_data[k][0] == 'down': aim += my_data[k][1]

   
print (horz, depth)
print (horz * depth)
