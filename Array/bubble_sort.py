
number = list(map(int, input().split()))

def bubble_sort(array): # 버블 정렬
    for i in range(len(array)-1): # 배열의 길이 -1 회전, 마지막에는 전부 정렬되어있다.
        for j in range(0,len(array)-1-i): # 한 회전이 끝날떄마다 마지막 자료를 제외한다.
            if array[j]>array[j+1]: # 이웃을 비교 이전 인덱스가 더 크다면
                array[j],array[j+1] = array[j+1],array[j] # 교환

bubble_sort(number)

print(number)

