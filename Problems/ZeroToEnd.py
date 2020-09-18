# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    array = [str(i) for i in array]
    c = 0
    for i in array:
        if i == '0':
            c += 1
            array.pop(array.index(i))
    array.append(['0']*c) 
    print(array)

move_zeros([False,1,0,1,2,0,1,3,"a"])
