#!/usr/bin/python


def is_part_of_set(n):
    """ returns True if the provided number is a Prime number
    https://en.wikipedia.org/wiki/Prime_number
    """
    
    if not isinstance(n,int):
        print('error, this function expects an integer')
        return None
    if n <2 :
        return False
    
    for i in range(2,1+(n//2)):
        if n%i == 0:
            return False
    return True
        
