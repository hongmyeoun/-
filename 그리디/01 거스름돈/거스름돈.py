# 거스름돈
# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한이 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# test case 1
# N = 1260
# 받을 동전의 최소 갯수 = 6개

import time
start_time = time.time() # 측정 시작

# 프로그램 소스코드
def solution(N):

    coin_type = [500, 100, 50, 10]
    result = 0
    for coin in coin_type:
        result += N // coin
        N %= coin

    return result

print(solution(1260))

end_time = time.time() # 측정 종료
print("time :", end_time - start_time)

# 의사코드
    # 지불받은 돈을 가장큰 500원부터 나눠서 몫을 저장

# 시간 복잡도는 화폐의 종류를 K라고 했을때, O(K)이다.
# 거스름돈 N은 없기때문.