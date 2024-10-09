import sys
origin = sys.stdin.readline().rstrip() 
target = sys.stdin.readline().rstrip()
o_list, t_list = list(origin), list(target)

def find_lcs(a, b):
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

    for a_idx in range(1, len(a)+1):
        for b_idx in range(1, len(b)+1):
            if a[a_idx-1] == b[b_idx-1]:
                dp[a_idx][b_idx] = dp[a_idx-1][b_idx-1] + 1
            else:
                dp[a_idx][b_idx] = max(dp[a_idx-1][b_idx], dp[a_idx][b_idx-1])
    return dp[len(a)][len(b)]

def find_long(a,b):
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        dp[i][0] = i
    for i in range(len(b)+1):
        dp[0][i] = i
    print(dp)

    for a_idx in range(1, len(a)+1):
        for b_idx in range(1, len(b)+1):
            if a[a_idx-1] == b[b_idx-1]:
                dp[a_idx][b_idx] = dp[a_idx-1][b_idx-1] + 1
            else:
                dp[a_idx][b_idx] = min(dp[a_idx-1][b_idx]+1, dp[a_idx][b_idx-1]+1)
    print(dp)
    return dp[len(a)][len(b)]

def find_dist(a,b):
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        dp[i][0] = i
    for i in range(len(b)+1):
        dp[0][i] = i

    for a_idx in range(1, len(a)+1):
        for b_idx in range(1, len(b)+1):
            if a[a_idx-1] == b[b_idx-1]:
                dp[a_idx][b_idx] = dp[a_idx-1][b_idx-1]
            else:
                dp[a_idx][b_idx] = min(dp[a_idx-1][b_idx]+1, dp[a_idx][b_idx-1]+1, dp[a_idx-1][b_idx-1]+1)
    return (dp[len(a)][len(b)])


print(find_dist(o_list, t_list))