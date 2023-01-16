
num = int(input())

numbers = []
for i in range(num):
    numbers.append(list(map(int, input().split())))

nums = [[0 for i in range(100)] for j in range(100)] # 100 x 100 도화지를 만든다.
def color_paper(array):
    sum = 0
    for k in range(num):
        x = array[k][0] # 앞서 받은 x값
        y = array[k][1] # 앞서 받은 y값
        for n in range(x,x+10): # 가로 세로 길이가 10이므로 10만큼 증가
            for j in range(y,y+10):
                if nums[n][j] != 1: # 이미 1이 아니라면
                    nums[n][j] = 1 # 1로 바꿔준다.
                    sum += 1 # 1을 더해줌 (결과에) 즉, 겹치는 부분은 빠지게 된다. 두번째에 1인 지점을 들리면 증가가 안되므로
    print(sum)

color_paper(numbers)


# 색종이가 겹치는 경우의 수는 굉장히 많다.
# 그래서 100 x 100 2차원 배열을 만들어서 문제를 해결하는 방법은 굉장히 신선했다.