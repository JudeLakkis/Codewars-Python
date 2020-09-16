# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    x, y = 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                x += 1
            elif i == 's':
                x -= 1
            elif i == 'e':
                y += 1
            elif i == 'w':
                y  -= 1
        if (x, y) == (0, 0):
            return True
    return False

test = ['n','s','n','s','n','s','n','s','n','s']
test2 = ['w','e','w','e','w','e','w','e','w','e','w','e']
print(is_valid_walk(test))
print(is_valid_walk(test2))
