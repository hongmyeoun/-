n = int(input())

def reverseArray(n):
    array = []
    for i in range(n):
        array.append(int(input()))

    array.sort(reverse=True)

    print(" ".join(map(str, array)))

reverseArray(n)