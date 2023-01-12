#아직 진행중
# 하다가 알바땜에 자러감

num = int(input())

numbers = []
for i in range(num):
    numbers.append(list(map(int, input().split())))

nums = [[0 for i in range(100)] for j in range(100)]
def color_paper(array):
    sum = 0
    for k in range(num):
        x = array[k][0]
        y = array[k][1]
        for n in range(x,x+10):
            for j in range(y,y+10):
                if nums[n][j] == 1:
                    nums[n][j] = 2
                else:
                    nums[n][j] = 1

    print((100 * num) - sum)

color_paper(numbers)