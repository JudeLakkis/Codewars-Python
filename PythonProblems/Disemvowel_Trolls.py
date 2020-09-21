# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(sen):
    return ''.join([i for i in sen if i.lower() not in 'a e i o u'.split(' ')])

test = "This website is for losers LOL!"
print(disemvowel(test))
