my_maze = []

with open('day05\input.txt', 'rt') as file:
    for line in file:
        my_maze.append(int(line.strip()))
file.close()

def FindStepsOutOfMaze(maze):
    my_steps = my_index = next_index = 0

    while my_index < len(maze):
        my_steps += 1
        next_index = my_index + maze[my_index]
        maze[my_index] += 1
        my_index = next_index

    return my_steps

print(FindStepsOutOfMaze(my_maze))
