from collections import deque

q = deque()
n = int(input())



for i in range(n):
    q.append(i+1)


while len(q) != 1:
    tmp = 0
    q.popleft()
    a = q.popleft()
    q.append(a)



print(q[0])

# deque로 풀었음 2023/2/16