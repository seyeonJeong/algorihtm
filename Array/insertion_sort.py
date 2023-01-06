
number = list(map(int, input().split()))

tmp = 0
def insertion_sort(number): # 삽입 정렬 함수
    for i in range(len(number)-1): # 두번째부터 시작하니까 4회 반복
        key = i+1 # key값은 현재 비교하고 싶은 수
        p_key = key - 1 # p_key는 key와 비교할 수
        while True: # 배열의 맨 첫번째까지 반복한다.
            if number[key] < number[p_key]: # 만약 key값보다 p_key값이 더 크면 자리를 바꿔준다
                tmp = number[key]
                number[key] = number[p_key]
                number[p_key] = tmp
                key -= 1 # 삽입 정렬은 무조건 이전으로만 이동하기 때문에 -1을 해준다.
                p_key -= 1 # p_key값또한 key값과 동일하게 -1
            else: # 크지않으면 그냥 p_key값만 -1을 진행한다.
                p_key -= 1
            if p_key == -1: # 만약 p_key값이 -1이 된다면 첫번째 인덱스까지 확인한 것
                break

insertion_sort(number)

print(number)

# 다른 사람 코드인데 코드 줄 차이 .. 
# def insertion_sort(number):
#     for i in range(1,len(number)):
#         for j in range(i,0,-1): # 이게 있는지 몰라서 코드가 굉장히 길어졌다. 
#             if number[j-1] > number[j]:
#                 number[j-1], number[j] = number[j], number[j-1] # swap 또한 이렇게 진행하면 된다. 기억하자

