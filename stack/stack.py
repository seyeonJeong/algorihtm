
class stack:
    def __init__(self): # init
        self.item = []
    def push(self,n): # stack의 push 그냥 계속 쌓임
        self.item.append(n)
    def pop(self): # pop LILO 이므로 마지막거 pop
        tmp = self.item[-1]
        self.item.remove(self.item[-1])
        return tmp
    def peek(self): # 마지막 원소를 pop하지않고 출력
        return self.item[-1]
    def empty(self): # list가 비어있는지 확인 비어있으면 true 출력
        if len(self.item) == 0:
            print('True')
        else:
            print('False')
    def search(self, o): # 원소를 탐색하고 그 인덱스를 반환
        for i in range(len(self.item)):
            if self.item[i] == o:
                return i


sk = stack() # 객체 생성
print(sk)

print(sk.empty())
sk.push(7)
sk.push(8)
sk.push(9)

print(sk.item)

print(sk.pop())
print(sk.item)

print(sk.search(8))
