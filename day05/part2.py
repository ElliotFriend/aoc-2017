my_input = open('day05\input.txt', 'rt')
my_maze = []
for l in my_input:
    my_maze.append(int(l.strip()))
print(my_maze)
my_steps = 0
my_index = 0
next_index = 0
while my_index < len(my_maze):
    my_steps += 1
    next_index = my_index + my_maze[my_index]
    if my_maze[my_index] >= 3:
        my_maze[my_index] -= 1
    else: my_maze[my_index] += 1
    my_index = next_index
print(my_steps)
