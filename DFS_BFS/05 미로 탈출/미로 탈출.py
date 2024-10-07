from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향 (좌 우 상 하)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) 

    # 큐가 빌 때 까지
    while queue:
        x, y = queue.popleft() # 이전 방문위치 불러옴
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1: # 첫 방문시
                graph[nx][ny] = graph[x][y] + 1 # 해당 위치에 값 1 증가
                queue.append((nx, ny)) # 해당 자리 저장
    
    # 가장 오른쪽 아래까지의 최단 거리 변환
    return graph[n - 1][m - 1]

print(bfs(0, 0))