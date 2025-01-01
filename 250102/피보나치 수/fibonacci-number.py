import sys
input= sys.stdin.readline

n = int(input())

fibo = [0,1,1]
if(n > 2):
    for idx in range(3,n+1):
        val = fibo[idx-1] + fibo[idx-2]
        fibo.append(val)

print(fibo[n])