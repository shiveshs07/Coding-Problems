if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        elem = int(input())
        if elem in arr:
            print(arr.index(elem))
        else:
            print(-1)
        t = t - 1
