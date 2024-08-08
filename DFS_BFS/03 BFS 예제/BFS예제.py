from collections import deque

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 1노드부터 시작했을때 방문한 노드순서
bfs(graph, 1, visited)

# bfs의 동작 원리는 너비를 우선으로 탐색하는 방식으로 가까운 거리에 있는 노드들을 먼저 탐색하는 방식이다.
# collections의 deque를 이용한다.
# 큐로 값을 탐색을 한다.
# 1. 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 방문했던 시작 노드를 꺼내고, 인접 노드를 모두 큐에 삽입
# 3. 인접노드도 2와 같이 방문하면 꺼내고 인접노드를 큐에 삽입, 이때 1에서 인접했던 노드(즉 가까운 노드들)를 먼저 방문
# 4. 큐가 빌 때까지 반복

# bfs는 큐를 이요하고 dfs는 스택을 이용하며, bfs는 큐자료구조를 이요하고, dfs는 재귀함수를 이용해 구현한다.