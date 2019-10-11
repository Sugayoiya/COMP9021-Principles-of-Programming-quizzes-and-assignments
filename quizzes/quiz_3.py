# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    return {}
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')







d = { 1:[(1,2),(2,3)], 2:[(2,3)], 4:[(4,5)], 3:[(3,4)] }
for step_size in sorted(d):
    print("step_size:",step_size)
    print(d[step_size])
    for nb_steps, nb_stairs in d[step_size]:
        print(nb_stairs,'stairs',nb_steps,'steps')

                

def check_sum(i, j, final_i, final_j, size):
    sum = check[i][j]
    flag = 1 # this flag let right down in turn
    count = 0 # check  whether lenth is satisfied
    step_right = (final_j - j)//(size - 1)  # how many time go right
    step_down = (final_i - i)//(size - 1) # how many time go down
    for steps in range(step_down+step_right):
        if flag == 1:
            temp = right_sum(i,j,size)
            if temp:
                i = temp[0]
                j = temp[1]
                size = temp[2]
                flag = -flag
                count += 1
            else:
                break
        else:
            temp = down_sum(i,j,size)
            if temp:
                i = temp[0]
                j = temp[1]
                size = temp[2]
                flag = -flag
                count += 1
            else:
                break
    if count == ( step_down + step_right ):
        return size, step_down # size = size   step_down = steps
    

    
# if  not satisfy, right_sum = false, down_sum = false
def right_sum(i, j, size):
    sum = check[i][j]
    for r_idex in range(size-1):
        j+=1
        sum += check[i][j]
    if sum == size:
        return [i,j,size]
    
def down_sum(i, j, size):
    sum = check[i][j]
    for c_idex in range(size-1):
        i+=1
        sum += check[i][j]
    if sum == size:
        return [i,j,size]