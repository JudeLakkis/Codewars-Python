# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(credit):
    return "#" * len(credit[:-4])+credit[-4:]

maskify("")
