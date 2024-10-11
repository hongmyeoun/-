n = int(input())

def score(n):
    array = []
    for i in range(n):
        inputs = input().split()
        array.append((inputs[0], int(inputs[1])))

    array.sort(key= lambda x: x[1])

    print(" ".join(str(i[0]) for i in array))

score(n)