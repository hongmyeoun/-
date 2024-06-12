# 나의 풀이

# 1시간 = 60분
# 1분 = 60초

def soultion():
    n = int(input())

    count = 0

    for hour in range(n+1):
        for min in range(60):
            for sec in range(60):
                if "3" in str(sec) or "3" in str(min) or "3" in str(hour):
                    count += 1

    print(count)
# 기어가 맞물리는 것처럼 생각하다가 오래걸렸다...3중 포문하고 가장 내부에서만 조건을 확인하면 되는것을...

# 해설
def str_plus_soultion():
    n = int(input())

    count = 0

    for hour in range(n+1):
        for min in range(60):
            for sec in range(60):
                if "3" in str(sec) + str(min) + str(hour):
                    count += 1

    print(count)
# 맞다 그냥 str을 더해주면 연결되니깐 이렇게 할껄 몰랐다.