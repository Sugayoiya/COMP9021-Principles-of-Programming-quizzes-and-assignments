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
#
# Written by *** and Eric Martin for COMP9021

# this file is lost

class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        if len(args) == 0:
            if length == None:
                self.args = []
            elif length < 0 :
                raise PermutationError('Cannot generate permutation from these arguments')
            else:
                self.args = [ generate for generate in range(1,length+1) ]
        elif len(args) == 1:
            if args ==(1,):
                self.args = list(args)
            else:
                raise PermutationError('Cannot generate permutation from these arguments')
#             if type(args[0]) == str or type(args[0]) == list:
#                 raise PermutationError('Cannot generate permutation from these arguments')
#             else:
#                 self.args = list(args)
#                 print('len(args) :',len(args) )
        elif len(list(args)) >1:
            compare_list = [ a for a in range(1,len(args)+1) ]
            if sorted(list(args)) != sorted(compare_list):
                raise PermutationError('Cannot generate permutation from these arguments')
            else:
                if length == None:
                    self.args = list(args)
                elif len(list(args)) != length:
                    raise PermutationError('Cannot generate permutation from these arguments')
                else:
                    self.args = list(args)
#         print(self.args)

        # start calculate circles
        temp_set = set([])
        i = 0
        circle = []
        full_set = set(self.args)
        circle_dict = defaultdict(list)
        while len(full_set - temp_set)!=0:
#             print(self.args[i])
#             print(self.args.index(self.args[i]) + 1)
            for e in (full_set - temp_set):
                temp_set.add(e)
                circle.append(e)
                while (self.args[e-1] not in temp_set) :
                    temp_set.add(self.args[e-1]  )
                    circle.append(self.args[e-1]  )
                    e = self.args[e-1] 
#                     print(temp_set)
#                     print(circle)
                circle_dict[max(circle)].append(circle[circle.index(max(circle)):] + circle[:circle.index(max(circle))])
                circle = []
                break
#         print(circle_dict)
        self._circle = circle_dict  # circle dict
        self.nb_of_cycles = len(self._circle)
            
    def __len__(self):
        return len(self.args)

    def __repr__(self):
        output = ''
        if len(self.args)>1:
            output = output+', '.join(str(e) for e in self.args)
        elif len(self.args)==1:
            output = output + str(self.args[0]) +','
        else:
            output = ''
        return f'Permutation({output})' 
        # Replace pass above with your code

    def __str__(self):
        output = ''
        if len(self._circle)>0:
            for e in sorted(self._circle):
                output += '('
                output += ' '.join(str(node) for node in self._circle[e][0])
                output += ')'
            return output
        else:
            return '()'
        # print circles
        
    def __mul__(self, permutation):
        if len(self.args) != len(permutation.args):
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            temp_1 = self.args.copy()
            temp_2 = permutation.args.copy()
            temp_1.insert(0,0)
            temp_2.insert(0,0)
            final = []
            for i in range(1,len(temp_1)):
                final.append(temp_2[temp_1[i]])  
            return Permutation(*final)
        # Replace pass above with your code

    def __imul__(self, permutation):
        if len(self.args) != len(permutation.args):
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            temp_1 = self.args.copy()
            temp_2 = permutation.args.copy()
            temp_1.insert(0,0)
            temp_2.insert(0,0)
            final = []
            for i in range(1,len(temp_1)):
                final.append(temp_2[temp_1[i]])  
            self = Permutation(*final)
            return self
        # Replace pass above with your code

    def inverse(self):
        temp = self.args.copy()
        new_list = []
        for e in temp:
            new_list.append(temp.index(temp.index(e)+1)+1)
        return Permutation(*new_list)
        # Replace pass above with your code
    # Insert your code for helper functions, if needed






                
        
