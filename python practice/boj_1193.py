
n = int(input())

line = 1

while n>line: # 1씩 개수가 증가하므로 몇번째 줄의 몇번째 인지 알수 있다.
    n -= line
    line += 1

if line%2 == 0: # 짝수 줄이면 x가 오름차순
    x = n
    y = line - n+1
else: # 홀수 줄이면 y가 내림차순
    x = line-n+1
    y = n

print(x,y, sep='/')
