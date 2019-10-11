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
from collections import defaultdict
from time import time

from stack_adt import *

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def hasChild(L,x,y,dire = '0'):
    direction = {'0': [[0,1,2,3],lambda x,y:[x-1,y]], \
             '1': [[1,2,3,0],lambda x,y:[x,y+1]],\
             '2': [[2,3,0,1],lambda x,y:[x+1,y]],\
             '3': [[3,0,1,2],lambda x,y:[x,y-1]]}
    if any( [x < 0 , x > 9 , y < 0 , y > 9]):
        return False
    values = 0
    fake = list((list(ele) for ele in L )) #important
    if fake[x][y] == -1:
        return False
    childrenList = defaultdict(list)
    # print(x,y)
    # display_grid()
    fake[x][y] = -1
    # e : directions
    for e in reversed(direction[dire][0]):
        colunm,row=(direction[str(e)][1](x,y))
        if all([colunm>=0, colunm<=9, row>=0, row<=9]):
            if fake[colunm][row] >= 0:
                # childrenlist{ (x,y) : [value, direction, copyGrid] }
                childrenList[(colunm,row)].append((fake[colunm][row],str(e),fake))
    return childrenList

def explore_depth_first(x, y, target):
    # pre-check
    summary = 0
    for e in grid:
        t = sum(e)
        summary += t
    if summary < target:
        return False
    # end pre-checking
    if grid[x][y] > target:
        return False
    if grid[x][y] == target:
        return [(x,y)]
    # print("create stack")
    stack = Stack()
    first_node = [[(x,y)], grid[x][y], '0', grid]
    stack.push(first_node)
    # print(first_node)
    while not stack.is_empty():
        # print("stack not empty")
        temp = stack.pop()
        path, states = temp[0],temp[1:]
        # print('path:',path,type(path))
        # print('*path:',*path)
        # print('states[0](value):',states[0])
        # print('states[1](direction):',states[1])
        # print('states[2](grid.copy):',states[2])
        if states[0] == target:
            # print("find it!")
            return path
        if states[0] > target:
            continue

        temp_children = hasChild(states[2],path[-1][0],path[-1][1],states[1])
        if temp_children:
            for child in temp_children:
                # childrenlist{ (x,y) : [value, direction, copyGrid] }
                # print('child:',child)
                temp_path = path[:]
                temp_path.append(child)
                # print('path:',path)
                # print('temp_path:',temp_path)
                values = states[0] + temp_children[child][0][0]
                # print('values:',values)
                stack.push([temp_path,values,temp_children[child][0][1],temp_children[child][0][2]])
                # print([path,values,temp_children[child][0][1],temp_children[child][0][2]])

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
start = time()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
elapsed = (time() - start)
print(elapsed)