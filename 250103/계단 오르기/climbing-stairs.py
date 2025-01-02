import sys
input = sys.stdin.readline

step = int(input())

answer = [0,0,1,1,1]

if step < 5:
    print(answer[step])
else:
    for idx in range(5,step+1):
        jump = answer[idx-3] + answer[idx-2]
        answer.append(jump % 10007)
    print(answer[step])