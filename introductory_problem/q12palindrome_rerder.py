def solve(S):
    N = len(S)
    ans = [' '] * N


    freq = [0] * 26
    for i in range(N):
        freq[ord(S[i]) - ord('A')] += 1


    cnt = 0
    for i in range(26):
        if freq[i] % 2 != 0:
            cnt += 1


    if cnt > 1:
        return "NO SOLUTION"

    left, right = 0, N - 1
    for i in range(N):
        if freq[ord(S[i]) - ord('A')] % 2 == 1:
            ans[N // 2] = S[i]
            freq[ord(S[i]) - ord('A')] -= 1
        while freq[ord(S[i]) - ord('A')] > 0:
            ans[left] = ans[right] = S[i]
            left += 1
            right -= 1
            freq[ord(S[i]) - ord('A')] -= 2

    return ''.join(ans)

if __name__ == "__main__":
    S = "AAZZAACACBA"
    print(solve(S))