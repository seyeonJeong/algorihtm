

num = int(input())

numbers = list(map(int, input().split()))

def find_max(array) : # 최댓값 함수
    max_num = -9999999 # 처음은 엄청 작은수
    for i in range(len(array)):
        if max_num < array[i] : # 만약 지금 최대값보다 더 큰 값이 발견되면 최대값을 변경
            max_num = array[i]
    return max_num

def find_min(array): # 최소값 함수
    min_num = 999999999 # 처음은 엄청 큰 수 아니면 첫번째 배열로 설정해도 괜찮을수도 있을 것 같다.
    for j in range(len(array)): # 만약 지금 최소값보다 더 작은 값이 발견되면 최소값을 변경
        if min_num > array[j] :
            min_num = array[j]

    return min_num

print(find_min(numbers), find_max(numbers))


