import sys
from collections import defaultdict

try:
    lowercase_letters = input('Enter between 3 and 10 lowercase letters:').split()
    lowercase_letters = ''.join(lowercase_letters)
    lowercase_letters = list(lowercase_letters)
    if len(lowercase_letters) >=3 and len(lowercase_letters) <=10:
        for s in lowercase_letters :
            if not s.islower():
                raise ValueError
    else:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

print(lowercase_letters)
words_filename = 'wordsEn.txt'

with open ( words_filename, 'r', encoding='utf-8') as wf:
	lines = wf.read()
	for line in lines:
		print(line)


# try:
#     arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
#     if arg_for_seed < 0 or length < 0 or max_value < 0:
#         raise ValueError
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()

# l1 = ['a','b','c']
# l2 = ['d', 'b','c','a']
# set(l1).issubset(set(l2))
# set(l2).issubset(set(l1))

# assign dict
val = dict([])
a = list('abcdefghijklmnopqrstuvwxyz')
b = list('25441655176352357212466757')
for k in a:
    for v in b:
        val[k] = v
        b.pop(0)
        break
val

# is_sub_list
a=['a','c','d']
b=['a','b','c','d']
ori_length = len(b)
if len(a)>len(b):
    print( 'false')
else:
    for i in range(len(a)):
        if a[i] in b:
            b.remove(a[i])
    if len(a) == ori_length - len(b):
        print ('a in b')
    else:
        print ('a not in b')