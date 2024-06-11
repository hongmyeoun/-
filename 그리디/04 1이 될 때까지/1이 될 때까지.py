# 나의 풀이
def soultion():
    print("입력")
    N, K = map(int, input().split())

    count = 0

    while N != 1:
        if N % K == 0 :
            N /= K
            count += 1
        else:
            N -= 1
            count += 1
    
    return count

print(f"출력\n{soultion()}")

# 단순 풀이 예시
def simple_soultion():
    n, k = map(int, input().split())

    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1
        
        n //= k
        result += 1
    
    while n > 1: # 남은 수에 대하여 1씩 빼는 로직인데 너무 비효율적으로 보임
        n -= 1
        result += 1

    print(result)

# 큰수가 들어오면 마지막 while문에서 나머지가 너무커서 문제가 난다.

# 다른 답안
def diff_soultion():
    n, k = map(int, input().split())
    result = 0

    while True:
        target = (n // k) * k # 나누어 떨어지면(배수면) target == n -> result는 +0
        result += (n - target) # 즉 나누어 떨어질 때 까지 1을 빼는 행위를 빠르게 생략
        n = target

        if n < k:
            break

        result += 1
        n //= k
    
    result += (n - 1) # break를 통해 나오기 때문에 처리가 안된 n값을 처리

    print(result)

    # 25 3
    # t = 24, r = 2, n = 8
    # t = 6, r = 5, n = 2
    # t = 0, r = 7, n = 2
    # r = 7 -(2 - 1) = 6

# 빠르게 1번 법칙을 생략하기 때문에 효율적이다.