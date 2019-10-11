from itertools import combinations

b = input('Input a number that we will use as available digits: ')
c = int(input('Input a number that represents the desired sum: '))
# print(type(b))
count = 0
L = []
for e in b:
    L.append(int(e))
for i in range(len(L)+1):
    for j in combinations(L,i):
        if sum(list(j)) == c:
            count += 1
if count < 1:
    print('There is no solution.')
elif count == 1:
    print('There is a unique solution.')
else:
    print(f'There is {count} solution.')