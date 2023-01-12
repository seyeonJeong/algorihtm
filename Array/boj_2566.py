

# 입력받을때, 하나하나 입력이 아닌 그냥 통으로 입력받아야 한다.
# 이때 그냥 빈 배열을 하나 선언하고 append를 시키는것이 방법
numbers = []

for i in range(9):
    numbers.append(list(map(int, input().split())))

def max(array):
    max = -9999999
    row = 0
    col = 0
    for j in range(9):
        for k in range(9):
            if max < array[j][k]:
                max = array[j][k]
                row = j+1
                col = k+1
    print(max)
    print(row, col)

max(numbers)