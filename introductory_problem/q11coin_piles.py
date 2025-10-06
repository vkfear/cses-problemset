def solve(A, B):


    if ((2 * A - B) % 3 != 0 or (2 * A - B) < 0
        or (2 * B - A) % 3 != 0 or (2 * B - A) < 0):

        return "NO\n"
    return "YES\n"

if __name__ == "__main__":
    Q = 3
    queries = [[2, 1], [2, 2], [3, 3]]
    print(Q)
    for query in queries:
        A, B = query[0], query[1]
        
        print(solve(A, B), end="")