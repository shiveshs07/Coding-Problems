t = int(input())
a = list(map(int, input().split()))
sa = a.sort()
temp1 = []
temp2 = []
for i, j in zip(a, sa):
    if i == j:
        temp1.append(i)
    else:
        temp2.append(i)
print(sum(temp1) - sum(temp2))

