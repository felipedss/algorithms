
'''
Example with number 16 (position = 0)
    10000
    00001
    =====
    10001  

Result == 17
'''
def set_bit(value, position):
    mask = 1 << position
    return value | mask

'''
Example with number 16 (position = 4)
    10000
    01111
    =====
    00000  

Result == 0
'''
def clear_bit(value, position):
    mask = 1 << position
    return value & ~mask      

'''
Example with number 16 (position = 4)
    10000
    10000
    =====
    00000  

Result == 0
'''
def flip_bit(value, position):
    mask = 1 << position
    return value ^ mask

'''
Example with number 16 (position = 1)
    10000  
    >>
    01000
    
    
    01000
    00001
    =====
    00000

Result == 0


Example with number 16 (position = 4)
    10000  
    >>
    00001
    

    00001
    00001
    =====
    00001

Result == 1

'''
def is_bit_set(value, position):
    shifted = value >> position
    return shifted & 1

def is_power_of_two(number):
    return number & number - 1 == 0 


assert is_bit_set(16, 4) == 1
assert flip_bit(16, 0) == 17
assert clear_bit(16, 4) == 0 
assert set_bit(16, 2) == 20



