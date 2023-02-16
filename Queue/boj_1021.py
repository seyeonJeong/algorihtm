from collections import deque

q = deque() #deque를 선언해준다
l,n = map(int,input().split())

cnt = 0
for i in range(l): # deque에 숫자로 채워줌
    q.append(i+1)

position = list(map(int, input().split())) # list형태로 담아준다

for j in position: # list의 숫자들을 하나하나 찾아낸다.
    while True: # 찾을때까지 반복
        if q[0] == j: # deque의 첫번에 찾는 숫자가 있으면 왼쪽에서 pop
            q.popleft()
            break
        else: # 없으면 찾아야함
            if q.index(j) > len(q)/2: # 여기서 2번을 쓸지 3번을 쓸지 정해줘야한다. 절반보다 크면 3번을 쓰는게 최소값
                while q[0] != j: # 찾을때까지 반복
                    q.appendleft(q.pop()) # 오른쪽에서 뽑아서 왼쪽에 둔다
                    cnt += 1
            else:
                while q[0] != j:
                    q.append(q.popleft()) # 왼쪽에서 뽑아서 오른쪽으로
                    cnt += 1

print(cnt)