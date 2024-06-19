def solution():
    n = input()
    x = int(n[1]) - 1
    y = int(ord(n[0])) - int(ord('a')) # a와 0을 매칭

    move = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)] # (x, y)

    result = 0
    for step in move:
        nx = x + step[0]
        ny = y + step[1]

        # x가 0~7 사이에 있으면서 y도 0~7사이에 있어야함
        if nx >= 0 and nx <= 7 and ny >= 0 and ny <= 7:
            result += 1

    print(result)

# move 마지막에 (1, 2)를 두번써서 계속 답이 안나왔다.