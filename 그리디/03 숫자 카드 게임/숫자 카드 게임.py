# 나의 풀이
# 입력부
def inputs():
    print("입력")

    N, M = map(int, input().split())

    array = []

    for i in range(N):
        row = list(map(int, input().split()))
        array.append(row)
    
    return array

# 메인 함수
def soultion():
    array = inputs()

    row_min = []

    for i in array:
        row_min.append(min(i))

    return max(row_min)


# 출력부
print(f"출력\n{soultion()}")

# 답안 min()
def min_soultion():
    n, m = map(int, input().split())

    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(result, min_value)

    print(result)

# 입력과 동시에 값을 비교하는 방법을 생각 못함.. 좋은듯?

# 답안 다중 for문
def two_for_soultion():
    n, m = map(int, input().split())

    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 10001 # 조건중 최대숫자
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)

    print(result)
# 구지 구지인가 싶다.