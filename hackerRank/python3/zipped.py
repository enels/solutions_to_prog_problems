n, x = map(int,input().split(" "))
l = []
for _ in range(x):
    l.append(list(map(float,input().split(" "))))
for n in zip(*l):
    print(f"{(sum(n)/len(n))}")
