quq = 0
d = []
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    maximum = max(a[quq])
    a[quq].clear()
    d.append(maximum)
    quq += 1
print(max(d))