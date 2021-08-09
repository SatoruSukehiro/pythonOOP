"""Python serial number generator."""

from typing import Counter


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self,start) :
        '''sets the start and then sets the adder this will allow you to create a number that adds one everytime the function is ran as well as creating a rest function'''
        self.start = self.add = start
        
    def generate(self):
        ''' add one everytime you run the function and returns that function make sure to return the number you get -1 to make srue you start at the start !!!! VERY IMPORTANT'''
        self.add += 1
        return self.add -1 
    def reset(self):
        return self.start

        

        
serial = SerialGenerator(50)  
    
print(serial.generate())
print(serial.generate())
print(serial.generate())
        
        
