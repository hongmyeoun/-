# 내 풀이
def soultion():
    N = int(input())

    move = list(input().split())

    X, Y = 1, 1

    for step in move:
        if X >= 1 and X <= N-1:
            if step == 'R':
                X += 1
            elif step == 'L':
                if X != 1:
                    X -= 1

        if Y >= 1 and Y <= N-1:
            if step == 'D':
                Y += 1
            elif step == 'U':
                if Y != 1:
                    Y -= 1
            


    print(Y, X)
# 그냥 생각나는대로 바로 푼 방식, IF가 많아서 보기 힘들다.

# 해설
def dxdy_soultion():
    n = int(input())
    move = input().split()
    x, y = 1, 1

    move_types = ['L', 'R', 'U', 'D'] # 움직임
    dx = [-1, 1, 0, 0] # 움직임과 매칭
    dy = [0, 0, -1, 1]

    for step in move:
        for i in range(len(move_types)):
            if step in move_types[i]:
                nx = x + dx[i] # 변위
                ny = y + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny > n: # 범위를 넘어가면 넘김
            continue

        x, y = nx, ny # 값 업데이트

    print(y, x) # 좌표가 반대