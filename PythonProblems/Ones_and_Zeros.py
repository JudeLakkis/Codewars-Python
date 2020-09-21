# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(struct):
    return int(''.join([str(i) for i in struct]), 2)

test = [0,0,1,1]
binary_array_to_number(test)
