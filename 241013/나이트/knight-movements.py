import sys
from collections import deque
input = sys.stdin.readline



INT_MAX = sys.maxsize
size = int(input())
start_r, start_c, end_r, end_c = list(map(int, input().split()))
start_r, start_c, end_r, end_c = start_r-1, start_c-1, end_r-1, end_c-1

location = [[0 for _ in range(size)] for _ in range(size)]
location[start_r][start_c] = 1

move_r = [-1,-2,-2,-1,+1,+2,+2,+1]
move_c = [-2,-1,+1,+2,-2,-1,+1,+2]

answer = INT_MAX
def bfs(r,c):
    global answer
    visited = [[False for _ in range(size)] for _ in range(size)]
    visited[r][c] = True
    save = deque([(r,c, 0)])
    while save:
        now_r, now_c, now_val = save.popleft()
        if now_r == end_r and now_c == end_c:
            answer = min(now_val, answer)
            return
        for m_idx in range(8):
            next_r, next_c = now_r + move_r[m_idx], now_c + move_c[m_idx]
            if 0 <= next_r < size and 0 <= next_c < size:
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    save.append((next_r,next_c,now_val+1))
bfs(start_r, start_c)
if answer == INT_MAX:
    print(-1)
else:
    print(answer)