def diffInSum(arr):
    sorted_arr = sorted(arr)
    sum1 = sum2 = 0
    for i, j in zip(arr, sorted_arr):
        if i == j:
            sum1 += i
        else:
            sum2 += i
    return sum1 - sum2

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        arr = list(int, input().split())
        result = diffInSum(arr)
        print(res)
