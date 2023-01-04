

hour, min = map(int, input().split())

time = int(input())


def result(min,time,hour):
    # time은 걸리는 시간인데 이를 60으로 나눈 몫과 나머지를 이용한다
    time_h = int(time/60)
    time_m = int(time%60)

    # 일단 시간을 증가시킨다.
    hour = hour + time_h
    min = min + time_m

    # 이후 우리가 흔히 아는 시간처럼 변경하는 작업을 한다.
    if(min >= 60):
        hour = hour + 1
        min = min - 60
    if (hour >= 24):
        hour = hour - 24

    print(hour,min)

result(min,time, hour)