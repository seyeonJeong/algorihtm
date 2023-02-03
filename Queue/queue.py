

class queue:
    front = 0
    rear = 0
    max = 8
    def __init__(self):
        self.item = [0 for i in range(self.max)]
        front = 0
        rear = 0
    def enqueue(self,n): # 큐의 삽입이다. 만약 큐가 꽉차있다면 print
        if queue.isfull(self) == 1:
            print("is full!")
        else:
            queue.rear = (queue.rear + 1) % queue.max # 모듈러 연산을 하는 이유 : 원형 큐이기 때문 , 원형 큐를 쓰는 이유는 선형 큐는 공간을 재활용 할 수 없다.
            print(queue.rear)
            self.item[queue.rear] = n

    def dequeue(self): # 큐의 삭제도 같은 모듈러 연산으로 계산된다.
        queue.front = (queue.front + 1) % queue.max
        print(self.item[queue.front])

    def isEmpty(self): # 비어있는지 확인 front와 rear이 같으면 비어있는 것이다.
        if queue.front == queue.rear:
            print("empty!")
        else:
            return 1
    def isfull(self): # 꽉찼는지 확인 모듈러 연산으로 확인 즉, rear 다음에 front가 있으면 꽉찬것
        if (queue.rear + 1) % queue.max == queue.front:
            return 1
    def size(self):
        print(self.rear - self.front)


qu = queue()

qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)

