import sys
input = sys.stdin.readline

turn_cnt, size, horse_cnt = list(map(int, input().split()))
turns = list(map(int, input().split()))

location = [1 for _ in range(horse_cnt)]

answer = 0
def play_game(now, result):
    global answer 

    if now == turn_cnt:
        answer = max(answer, result)
        return
    
    now_move = turns[now]
    for idx in range(horse_cnt):
        before = location[idx]
        if location[idx] != size:
            location[idx] = min(size, location[idx] + now_move)
            if location[idx] == size:
                play_game(now+1, result+1)
            else:
                play_game(now+1, result)
        location[idx] = before


play_game(0,0)
print(answer)