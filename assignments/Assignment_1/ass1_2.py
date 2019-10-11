import sys
from collections import deque

try:
    final_list = input('Input final configuration: ').split()
    final_list = ''.join(final_list)
    final_list = list(final_list)
    if sorted(final_list) != ['1', '2', '3', '4', '5', '6', '7', '8']:
        raise ValueError
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()

def row_exchange(L):
	temp = L[::-1]
	return(temp)
    
def right_circular_shift(L):
	temp = L.copy()
	temp.insert(0,temp.pop(3))
	temp.append(temp.pop(4))
	return(temp)

def middle_clockwise_rotation(L):
	temp = L.copy()
	temp.insert(1,temp.pop(6))
	temp.insert(5,temp.pop(3))
	return(temp)

initial_list = ['1', '2', '3', '4', '5', '6', '7', '8']
# change initial_list to final_list

# steps to the final list
steps = 0
check_deque = deque([])
# add initial list
check_deque.append((initial_list, steps))
flag = 0
temp =deque([])
result_set = set([])
# add initial element to check duplicates
result_set.add(tuple(initial_list))
while flag == 0 :
	# pop not satisfied element to generate next list
	for e in check_deque:
		if e[0] != final_list:
			temp.append(row_exchange(e[0]))
			temp.append(right_circular_shift(e[0]))
			temp.append(middle_clockwise_rotation(e[0]))
		else:
			if e[1] > 1:
				print(f'{e[1]} steps are needed to reach the final configuration.' )
				flag = 1
				break
			else:
				print(f'{e[1]} step is needed to reach the final configuration.' )
				flag = 1
				break
			
# 	print(temp)
	if flag == 0: 
		check_deque = deque([])
		steps += 1
		for ele in temp:
			if tuple(ele) not in result_set:
				result_set.add(tuple(ele))
				check_deque.append((ele,steps))
		temp = deque([])
