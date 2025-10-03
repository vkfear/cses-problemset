MOD = 10**9 + 7

def power(base, expo):
    ans = 1
    while expo:
        if expo & 1:
            ans = (ans * base) % MOD
        base = (base * base) % MOD
        expo >>= 1
    return ans

if __name__ == "__main__":
    N = 5
    print(power(2, N))