import sys
input = sys.stdin.readline

size = int(input())
zone = []
for _ in range(size):
    temp = list(map(int, input().split()))
    zone.append(temp)

dp = [[0 for _ in range(size)] for _ in range(size)]
dp[0][0] = zone[0][0]

for idx in range(1,size):
    dp[0][idx] = dp[0][idx-1] + zone[0][idx]
    dp[idx][0] = dp[idx-1][0] + zone[idx][0]

for r_idx in range(1,size):
    for c_idx in range(1,size):
        dp[r_idx][c_idx] = max(dp[r_idx][c_idx-1], dp[r_idx-1][c_idx]) + zone[r_idx][c_idx]

print(dp[size-1][size-1])