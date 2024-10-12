import sys
import heapq

input = sys.stdin.readline 

line_cnt = int(input())
save = []

for _ in range(line_cnt):
    start, end = list(map(int, input().split()))
    save.append((start,end))
save.sort()

answer = 0

def find(old_s, old_e, now_i, result):
    global answer 

    if now_i >= line_cnt:
        answer = max(answer, result)
        return 
    now_s, now_e = save[now_i]
    if old_s <= now_s <= old_e:
        if now_e <= old_e:
            find(now_s, now_e, now_i+1, result)
        else:
            find(old_s, old_e, now_i+1, result)
    else:
        find(old_s, old_e, now_i+1, result)
        find(now_s, now_e, now_i+1, result+1)


find(0,0,0,0)
print(answer)