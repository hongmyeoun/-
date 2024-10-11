n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for i in range(k):
    if a[0] < b[-1]:
        a[0], b[-1] = b[-1], a[0]
        a.sort()
        b.sort()

print(a)
print(sum(a))