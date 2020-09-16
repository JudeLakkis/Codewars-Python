# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(num):
   return sum([i for i in range(num) if i % 5 == 0 or i % 3 == 0])

print(solution(10))
