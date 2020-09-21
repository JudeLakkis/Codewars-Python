# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(struct):
    even = [i for i in struct if i % 2 == 0]
    if len(even) > 1:
        return [i for i in struct if i not in even][0]
    else:
        return even[0]

test = [2, 4, 6, 8, 10, 3]
test2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(test))
print(find_outlier(test2))


