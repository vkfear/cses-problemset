
def solve(N):
    if N == 0:
        return 0
    return N // 5 + solve(N // 5)



if __name__ == "__main__":
    
    N=30

    print(solve(N))
