#import sys
#sys.setrecursionlimit(10**8)

number = list(map(int,input().split()))

def merge(array, left, right): # 배열을 병합하는 코드

    mid = int((left+right)/2) # left+right/2일때 괄호를 안썼더니 오류가 계속 났다...... 괄호 중요
    l = left # 첫 시작
    r = mid + 1 # 중간 다음
    k = 0 # 새로운 배열의 가리키고 있는 곳
    tmp = [0 for i in range(left, right+1)] # 새로운 배열

    # 두 배열의 각 첫번째를 비교한다 왼쪽이 크면 r을 증가시키고 배열에 넣는다.
    # 이걸 계속 반복하는 느낌..
    # 중요한 점은 비교할때마다 r또는 l을 증가시킨다는 점과, 만약 l이 중간 지점을 넘어서면, 오른쪽 배열에 남은 모든 수를 그냥 다 배열에 넣는다.
    # 배열을 나누어서 정렬한다는 것 또한 중요하다.
    while True:
        if array[l] > array[r]:
            tmp[k] = array[r]
            k += 1
            r += 1
        else:
            tmp[k] = array[l]
            k += 1
            l += 1
        if l > mid:
            while True:
                tmp[k] = array[r]
                r += 1
                k += 1
                if k >= len(tmp):
                    break
            break
        elif r > right:
            while True:
                tmp[k] = array[l]
                l += 1
                k += 1
                if k >= len(tmp):
                    break
            break

    for i in range(0,(right-left) + 1):
        array[left+i] = tmp[i]
    print(tmp)
    print(array)



def merge_sort(number, left, right):
    # 재귀를 이용해서 범위를 하나의 원소만 남을때까지 반복한다. 이렇게 나눈 후에 하나하나 합치면서 정렬한다.
    if left >= right:
        return
    mid = int((left+right)/2)
    # 두개로 나눔.
    merge_sort(number,left,mid)
    merge_sort(number,mid+1,right)

    merge(number, left, right)


merge_sort(number, 0, len(number)-1)

