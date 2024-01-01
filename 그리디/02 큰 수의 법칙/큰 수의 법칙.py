import time

N, M, K = map(int, input().split())
array = list(map(int, input().split()))

start_time = time.time() # 측정 시작

def solution(N, M, K, array):
    array.sort()
    max = array[N-1]
    sec_max = array[N-2]
    return max*(M - M//K) + sec_max*(M//K)

print(solution(N,M,K,array))

end_time = time.time() # 측정 종료
print("time :", end_time - start_time)

# 결과 1
# 5 8 3
# 2 4 5 4 6
# 46
# time : 0.0

# 결과 2
# 5 7 2
# 3 4 3 4 3
# 28
# time : 0.0

# 의사코드
    # 받은 배열 정렬(오름차순)
    # 최댓값과, 그 다음값을 만듦
    # M번동안 최대값을 K번 더해주고 K번 더했으면, 그 다음값을 한번 더함
    # 그리고나서 다시 최대값을 K번 더해줌
    # -> M을 K로 나눔 | ex) 8 // 3 = 2 -> 두번은 sec_max값을 더해주는거임
    # -> max*(M - M//K) + sec_max*(M//K)

# 단순 답안
N, M, K = map(int, input().split())
array = list(map(int, input().split()))

def solution(N, M, K, array):
    array.sort()
    max = array[N-1]
    sec_max = array[N-2]
    result = 0
    while True:
        for i in range(K):
            if M == 0:
                break
            result += max
            M -= 1
        if M == 0:
            break
        result += sec_max
        M -= 1
    return result
# 이 답안은 M의 크기가 100억 이상에선 시간초과판정을 받을 수 있다.
# 따라서 다른 방식으로 풀이

def solution(N, M, K, array):
    array.sort()
    max = array[N-1]
    sec_max = array[N-2]
    count = int(M/(K+1))*K # M//(K+1)
    count += M % (K+1)

    result = 0
    result += (count)*max
    result += (M-count)*sec_max

# 내 풀이가 가장 간단한듯?