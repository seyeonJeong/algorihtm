import sys

n = int(sys.stdin.readline())
stack = [] # stack을 위한 배열
answer = [] # 정답을 위한 배열
cur = 1 # 탐색 변수
flag = 0 # 플래그 (정답을 출력하는데, 잘못된 경우 출력하면 안되기 때문)
for i in range(n):
    num = int(sys.stdin.readline()) # 하나하나씩 받아준다.
    while cur <= num: # 탐색변수가 받아온 값보다 작으면 그 값까지 push해줘야 한다.
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num: # 만약 탐색변수가 받아온값보다 커지게 되면 stack의 top을 체크함. 이때 찾으려는 수가 top이면 pop해준다.
        stack.pop()
        answer.append('-')

    else: # top이 아니면 방법이 없다. (이유는, 이미 stack에는 순차적으로 숫자가 채워지는데 이미 탐색변수가 찾으려는 숫자를 지나간 상황)
        print("NO")
        flag = 1 # flag를 1로 변경하고 break를 한다. 이때 NO만 출력되고 끝난다.
        break

if flag == 0: # 이 경우는 stack을 이용해서 정답을 만든 경우이다. 정답 배열을 출력한다.
    for i in answer:
        print(i)


# 실버2는 처음 도전해봤는데, 문제의 해결법을 찾아내는것이 쉽지 않았다. 대충 근접은 하지만 조건들을 모두 충족시키는 상황을 만들기가 어려웠다.


