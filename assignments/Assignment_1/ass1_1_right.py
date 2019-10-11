import sys

flag = 1
while flag:
	try:
	    goal_cell_num = input('Enter the desired goal cell number: ')
	except ValueError:
	    print('Incorrect value, try again')
	    # sys.exit()
	try:
	    goal_cell_num = int(goal_cell_num)
	    if goal_cell_num < 0:
	        raise ValueError
	    else:
	    	flag = 0
	except ValueError:
	    print('Incorrect value, try again')
	    # sys.exit()

# input die list
# -->
def to_the_right(L):
	temp = [0,0,0,0,0,0]
	# right front top
	temp[0] = L.pop(2)
	temp[1] = L.pop(1)
	temp[2] = L.pop(1)
	# opposite
	temp[3] = 7 - temp[0]
	temp[4] = 7 - temp[1]
	temp[5] = 7 - temp[2]
	L = temp.copy()
	return L

# |
# V
def forwards(L):
	temp = [0,0,0,0,0,0]
	# right front top
	temp[0] = L.pop(0)
	temp[1] = L.pop(1)
	temp[2] = L.pop(2)
	# opposite
	temp[3] = 7 - temp[0]
	temp[4] = 7 - temp[1]
	temp[5] = 7 - temp[2]
	L = temp.copy()
	return L

# <--
def to_the_left(L):
	temp = [0,0,0,0,0,0]
	# right front top
	temp[0] = L.pop(5)
	temp[1] = L.pop(1)
	temp[2] = L.pop(0)
	# opposite
	temp[3] = 7 - temp[0]
	temp[4] = 7 - temp[1]
	temp[5] = 7 - temp[2]
	L = temp.copy()
	return L

# ^
# |
def backwards(L):
	temp = [0,0,0,0,0,0]
	# right front top
	temp[0] = L.pop(0)
	temp[1] = L.pop(4)
	temp[2] = L.pop(0)
	# opposite
	temp[3] = 7 - temp[0]
	temp[4] = 7 - temp[1]
	temp[5] = 7 - temp[2]
	L = temp.copy()
	return L


def directory_count(i,L):
	path = {'right':0, 'left':0, 'forwards':0, 'backwards':0}
	count = 0
	if i == 1:
		return L
	else:
		count = 1
		i = i - 1
		while i > 0:
			# right
			if i  >= count :
				path['right'] = count
				i = i - count
				#
				for steps in range(path['right']):
					L = to_the_right(L)
			else:
				path['right'] = i 
				i = 0
				for steps in range(path['right']):
					L = to_the_right(L)
				break
			# forwards
			if i  >= count :
				path['forwards'] = count
				i = i - count
				#
				for steps in range(path['forwards']):
					L = forwards(L)
				count += 1
			else:
				path['forwards'] = i 
				i = 0
				#
				for steps in range(path['forwards']):
					L = forwards(L)
			# left
			if i  >= count :
				path['left'] = count
				i = i - count
				#
				for steps in range(path['left']):
					L = to_the_left(L)
			else:
				path['left'] = i 
				i = 0
				for steps in range(path['left']):
					L = to_the_left(L)
				break
			# backwards
			if i >= count :
				path['backwards'] = count
				i = i - count
				count += 1
				for steps in range(path['backwards']):
					L = backwards(L)
			else:
				path['backwards'] = i 
				i = 0
				for steps in range(path['backwards']):
					L = backwards(L)
	return L

L = [1,2,3,6,5,4]
L = directory_count(goal_cell_num,L)
print(f'On cell {goal_cell_num}, {L[2]} is at the top, {L[1]} at the front, and {L[0]} on the right.')