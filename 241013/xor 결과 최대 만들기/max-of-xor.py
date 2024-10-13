import sys
from itertools import combinations
input = sys.stdin.readline

num_cnt, choice_cnt = list(map(int, input().split()))
nums = list(map(int, input().split()))



choice_nums = list(combinations(nums, choice_cnt))

answer = 0
for now in choice_nums:
    temp = now[0]
    for num in now[1:]:
        temp = temp^num
    answer = max(answer, temp)

print(answer)