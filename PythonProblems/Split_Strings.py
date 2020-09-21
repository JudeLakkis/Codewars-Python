# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(struct):
    if len(struct) % 2 != 0:
        struct += '_'
    return [''.join((struct[i], struct[i+1])) for i in range(0, len(struct), 2)]

solution("asdfadsf")
