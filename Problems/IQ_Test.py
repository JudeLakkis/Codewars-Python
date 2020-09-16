# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(struct):
    even = [struct.split(' ').index(i) for i in struct.split(' ') if int(i) % 2 == 0]
    odd = [struct.split(' ').index(i) for i in struct.split(' ') if int(i) % 2 != 0]
    if len(even) > len(odd):
        return odd[0] + 1
    else:
        return even[0] + 1

print(iq_test("1 1 1 1 1 2 3 3 5 5 7 9"))
