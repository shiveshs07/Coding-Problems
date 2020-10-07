if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        i = 0
        while i < n:
            temp = arr[i : i + k]
            temp.reverse()
            print(*temp, end=" ")
            i += k
        print()
        t = t - 1
