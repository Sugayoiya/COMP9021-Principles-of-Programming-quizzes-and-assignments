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
        if isinstance(args, str):
            raise PermutationError('Cannot generate permutation from these arguments')
        elif isinstance(args,list):
            if len(args)!= length:
                raise PermutationError('Cannot generate permutation from these arguments')
            else:
                self.args = args
                self.length = length
            


    def __repr__(self):
        return self.args






                
        
