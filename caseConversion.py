t = input()
temp = []
tempi = 0
for i in range(1, len(t)):
    if t[i].isupper():
        temp.append(t[tempi:i])
        temp.append("_")
        tempi = i
temp.append(t[tempi:])
ans = ""
for i in temp:
    ans += i
print(ans.lower())
