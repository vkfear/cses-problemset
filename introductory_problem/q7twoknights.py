def two_knights(K):

    total_ways= ((K*K)*((K*K)-1)) /2

    attack_ways = 4 * (K - 1) * (K - 2)

    ans = total_ways-attack_ways

    return ans 

if __name__ == "__main__":
    N = 8
    
    for K in range(1, N + 1):
        print(two_knights(K), end=" ")

