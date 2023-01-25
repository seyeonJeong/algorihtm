import sys

n = int(sys.stdin.readline())

stack = []
sum = 0
for i in range(n):
    num = int(sys.stdin.readline())

    if num == 0: # 만약 수가 0이면 스택에서 pop
        sum -= stack.pop()

    else: # 0이 아니면 push
        stack.append(num)
        sum += num

print(sum)

# 스택 칸에 있지만, 가장 최근의 수를 빼고 넣는 다는 것에서 스택을 생각해낼수 있다.