import sys
input = sys.stdin.readline

size = int(input())
location = []
for _ in range(size):
    temp = list(map(int, input().split()))
    location.append(temp)

move_r = [+1,0]
move_c = [0,+1]


answer = 0
def dfs(r, c, result):
    global answer

    if r == size-1 and c == size-1:
        answer = max(answer, result)
        return
    for m_idx in range(2):
        next_r, next_c = move_r[m_idx]+r, move_c[m_idx]+c
        if 0 <= next_r < size and 0 <= next_c < size:
            if result > location[next_r][next_c]:
                dfs(next_r, next_c, location[next_r][next_c])
            else:
                dfs(next_r, next_c, result)

dfs(0,0,location[0][0])
print(answer)