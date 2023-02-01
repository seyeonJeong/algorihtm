

class queue:
    front = 0
    rear = 0
    max = 8
    def __init__(self):
        self.item = [0 for i in range(self.max)]
        front = 0
        rear = 0
    def enqueue(self,n):
        queue.rear = (queue.rear + 1) % queue.max
        self.item[queue.rear] = n


    def dequeue(self):
        print(self.item[queue.front])
        queue.front = (queue.front + 1) % queue.max

    def isEmpty(self):
        if queue.front == queue.rear:
            print("empty!")
        else:
            print("No!")
    def size(self):
        print(self.rear - self.front)


qu = queue()

print(qu)

qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(1)

print(qu.item)

qu.dequeue()
print(qu.item)
qu.dequeue()
print(qu.rear)
qu.enqueue(3)
qu.enqueue(4)
print(qu.item)

print(qu.rear)

qu.size()

#..ing