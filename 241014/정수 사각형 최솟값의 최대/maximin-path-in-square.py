import sys
input = sys.stdin.readline

size = int(input())
location = []
for _ in range(size):
    temp = list(map(int, input().split()))
    location.append(temp)

INT_MAX = sys.maxsize
move_r = [+1,0]
move_c = [0,+1]
visited = [[False for _ in range(size)] for _ in range(size)]
dp = [[INT_MAX for _ in range(size+1)] for _ in range(size+1)]


answer = 0

for r in range(size+1):
    for c in range(size+1):
        dp[r][c] = min(location[r-1][c-1], max(dp[r-1][c], dp[r][c-1]))


print(dp[size][size])