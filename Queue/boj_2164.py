
n = int(input())

queue = [0 for i in range(n)]
rear = 0
front = 0

for i in range(n):
    queue[i] = i+1
    rear += 1


while rear != (front+1):
    tmp = 0
    queue[front] = 0
    front += 1
    cur = front
    while (cur+1) != rear:
        queue[cur],queue[cur+1] = queue[cur+1],queue[cur]
        cur += 1


print(queue[-1])

# 계속 틀렸다해서 결과를 보니 deque를 쓰라고 한다.. deque 공부하고 다시 풀어야함