# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *

# move = {'up': lambda x, y: x-1, y, 
#         'right':lambda x, y: x, y+1,
#         'down': lambda x, y: x+1, y,
#         'left': lambda x, y: x, y-1}

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

stack = Stack()
path = []
temp = []
flag = 0 
temp_sum = 0
def explore_depth_first(x, y, target):
    global temp_sum
    if any( [x < 0 , x > 9 , y < 0 , y > 9]):
        return False
    if grid[x][y] == -1:
        return False
    if grid[x][y] > target:
        return False
    if temp_sum + grid[x][y] > target:
        return False
    stack.push(grid[x][y])
    global flag
    # which directory
    if len(path) != 0 and x < path[-1][0]:
        flag = 0
    if len(path) != 0 and y > path[-1][1]:
        flag = 1
    if len(path) != 0 and x > path[-1][0]:
        flag = 2
    if len(path) != 0 and y < path[-1][1]:
        flag = 3
    path.append((x,y))
    grid[x][y] = -1
    global temp
    while not stack.is_empty():
        temp.append(stack.pop())
    temp.sort(reverse = True)
    temp_sum = sum(temp)
    print(flag)
    while  temp_sum!= target and temp_sum < target:
        for e in temp:
            stack.push(e)
        temp = []
        if flag == 0:
            return explore_depth_first(x-1, y, target)or\
                    explore_depth_first(x, y+1, target)or\
                    explore_depth_first(x+1, y, target)or\
                    explore_depth_first(x, y-1, target)
        if flag == 1:
            return explore_depth_first(x, y+1, target)or\
                    explore_depth_first(x+1, y, target)or\
                    explore_depth_first(x, y-1, target)or\
                    explore_depth_first(x-1, y, target)
        if flag == 2:
            return explore_depth_first(x+1, y, target)or\
                    explore_depth_first(x, y-1, target)or\
                    explore_depth_first(x-1, y, target)or\
                    explore_depth_first(x, y+1, target)
        if flag == 3:
            return explore_depth_first(x, y-1, target)or\
                    explore_depth_first(x-1, y, target)or\
                    explore_depth_first(x, y+1, target)or\
                    explore_depth_first(x+1, y, target)
    return path
    # Replace pass above with your code


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]

print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
