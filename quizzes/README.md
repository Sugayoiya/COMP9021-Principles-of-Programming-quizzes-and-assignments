##### quiz1

```
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
```


##### quiz2

```
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
```

##### quiz3

```
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
```

##### quiz4

```
# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.
```

##### quiz5

**Sample outputs**
```
$ python3 quiz_5.py
Enter four nonnegative integers: 0 1 4 4
Here is the grid that has been generated:
1 1 0 1
1 1 1 1
1 0 0 1
0 0 1 0
The number of paths from 1 to 1 is: 10

$ python3 quiz_5.py
Enter four nonnegative integers: 0 2 4 4
Here is the grid that has been generated:
1 1 0 1
2 1 1 1
1 1 2 0
2 0 1 0
The number of paths from 1 to 1 is: 3
The number of paths from 1 to 2 is: 7

$ python3 quiz_5.py
Enter four nonnegative integers: 0 3 4 6
Here is the grid that has been generated:
3 3 0 2 3 3
2 3 2 1 1 2
1 0 2 1 2 0
0 2 3 0 2 3
The number of paths from 1 to 2 is: 2
The number of paths from 1 to 3 is: 6

$ python3 quiz_5.py
Enter four nonnegative integers: 0 4 5 8
Here is the grid that has been generated:
3 3 0 2 4 3 3 2
3 2 4 1 4 1 2 1
0 4 2 4 4 1 2 0
0 2 3 4 0 2 3 2
4 1 4 3 3 4 2 0
The number of paths from 1 to 2 is: 1
The number of paths from 1 to 3 is: 5
The number of paths from 1 to 4 is: 2

$ python3 quiz_5.py
Enter four nonnegative integers: 0 4 6 6
Here is the grid that has been generated:
3 3 0 2 4 3
3 2 3 2 4 1
4 1 2 1 0 4
2 4 4 1 2 0
0 2 3 4 0 2
3 2 4 1 4 3
The number of paths from 1 to 1 is: 2
The number of paths from 1 to 2 is: 1
The number of paths from 1 to 3 is: 5
The number of paths from 1 to 4 is: 1
```

##### quiz6
```
# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
```

##### quiz7

```
# Generates a linked list of a length determined by user input,
# consisting of random nonnegative integers whose upper bound is also determined
# by user input, and reorders the list so that it starts with all odd values and
# ends with all even values, preserving the order of odd and even values in the
# original list, respectively.
```

##### quiz8

```
# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
```

##### quiz9

```
# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
```

##### quiz10

```
# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
```
