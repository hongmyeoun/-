def solution():
    N, M = map(int, input().split())

    X, Y, direction = map(int, input().split())

    NM_map = [[0] * M for _ in range(N)]
    NM_map[X][Y] = 1 # 시작 좌표는 count 된것으로 처리
    game_map = []

    for i in range(int(M)):
        game_map.append(list(map(int, input().split())))

    # [북0 동1 남2 서3]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    count = 1 # 시작 좌표는 count 된것으로 처리
    turn_time = 0

    while True:
        direction = turn_left(direction)
        
        nx = X + dx[direction]
        ny = Y + dy[direction]

        # 회전하고 간 곳이 0이면(육지)
        if NM_map[nx][ny] == 0 and game_map[nx][ny] == 0:
            # 해당 장소를 바다로 변경(갓다고 표기)
            NM_map[nx][ny] = 1

            # 현재위치 변경
            X = nx
            Y = ny

            # 카운트 업
            count += 1

            # 회전회수 초기화
            turn_time = 0

            # 이어서 실행
            continue
        # 회전하고 갈곳이 없다면
        else:
            turn_time += 1

        # 갈 곳이 없다면
        if turn_time == 4:
            # 돌아간다(반대로)
            nx = X - dx[direction]
            ny = Y - dy[direction]

            # 돌아갈 땅이 있다면(육지면)
            if game_map[nx][ny] == 0:
                X = nx
                Y = ny
            # 돌아갈 땅이 없다면(바다면)
            else:
                break

            turn_time = 0

    print(count)

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    
    return direction

solution()