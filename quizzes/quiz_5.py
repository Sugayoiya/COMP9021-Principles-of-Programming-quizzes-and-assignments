from random import seed, randint
import sys
from collections import defaultdict, Counter


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

L = []
        
def get_length(i,j):
    global L
    length = 1
    if j  and (grid[i][j-1] - grid[i][j]) == 1:
#         print(i,j-1,'<--')
        length += get_length(i,j-1)
    if j < (width - 1) and  (grid[i][j+1] - grid[i][j]) == 1:
#         print(i,j+1,'-->')
        length += get_length(i,j+1)
    if i  and (grid[i-1][j] - grid[i][j]) == 1:
#         print(i-1,j,'^')
        length += get_length(i-1,j)
    if i < (height - 1) and  (grid[i+1][j] - grid[i][j]) == 1:
#         print(i+1,j,'v')
        length += get_length(i+1,j)
    if (j<=0 or (grid[i][j-1] - grid[i][j]) != 1) and (j>=(width -1) or (grid[i][j+1] - grid[i][j]) != 1)and ( i<=0 or (grid[i-1][j] - grid[i][j]) != 1) and (i>= (height-1) or (grid[i+1][j] - grid[i][j]) != 1):
        L.append(grid[i][j])
    return length

def get_paths():
    path = dict([])
    pathe = Counter
    for i in range(max_length+1):
        path[i] = 0
    del(path[0])
#     print(path)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                get_length(i,j)
#                 path[get_length(i,j)] += 1
#     print(path)
    path = dict(Counter(L))
    return path

try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
