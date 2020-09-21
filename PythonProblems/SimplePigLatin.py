# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(struct):
    return ' '.join([ str(i+i[0]+'ay')[1:] if i not in '! ? ;'.split(' ') else i for i in struct.split(' ')])

test = 'Pig latin is cool'
test2 = 'Hello world !'
print(pig_it(test))
print(pig_it(test2))
