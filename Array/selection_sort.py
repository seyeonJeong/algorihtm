

number = list(map(int, input().split())) # int형 띄어쓰기 구분으로 받는데 list 형으로 받는다.

def selection_sort(array) : # 선택 정렬 함수
    minindex = 0 # 최소값의 인덱스 값
    tmp = 0 # swap 연산시 필요한 변수
    for i in range(len(array)): # 기본 반복 (1회전, 2회전, 3회전 ...)
        minindex = i
        for j in range(i+1, len(array)) : # 세부 반복 (첫번째와 이후 최소값 찾는 반복)
            if array[minindex] > array[j] : # 만약 가장 작은 값이 새로 발견한 값보다 크면? 그 값이 최소
                minindex = j

        if array[i] > array[minindex] : # 만약 뒤의 값들 중 최소인 값이 현재 선택된 값보다 작으면? 자리를 바꿔야한다.
            tmp = array[minindex] # 자리 바꿈
            array[minindex] = array[i]
            array[i] = tmp
        print(array)

selection_sort(number)
