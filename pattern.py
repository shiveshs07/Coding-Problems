n = int(input())

res = ""

for i in range(n, 0, -1):
    j = n
    while j > 0:
        res = res + (str(j) + " ") * i
        j -= 1
    res += "$"

print(res)
