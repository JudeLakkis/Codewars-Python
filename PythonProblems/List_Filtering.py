# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(struc):
    return [i for i in struc if type(i) != str]

filter_list([1,2,'aasf','1','123',123])


