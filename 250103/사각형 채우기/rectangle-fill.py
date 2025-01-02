import sys
input = sys.stdin.readline

size = int(input())

answer = [0,1,2]
if size < 3:
    print(answer[size])
else:
    for idx in range(3,size+1):
        cnt = answer[idx-1] + answer[idx-2]
        answer.append(cnt % 10007)
    print(answer[size])