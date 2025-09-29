def total_moves(arr,N):

    ans = 0

    for i in range(1,N):
        if arr[i-1] > arr[i]:
            ans += (arr[i-1] - arr[i])
            arr[i] = arr[i-1]

    return ans

if __name__ == "__main__":

    N=5

    arr = [3,1,2,5,6]

    print(total_moves(arr,N))