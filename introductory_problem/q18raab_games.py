def solve_one(n, a, b):
   
    if a + b > n:
        print("NO")
        return
    if a + b == 0:
     
        print("YES")
        print(*range(1, n+1))
        print(*range(1, n+1))
        return

    if a == 0 or b == 0:
        print("NO")
        return

    A = list(range(1, n+1))          
    B = [0] * n
    used = [False] * (n+1)         

  
    start_draw = b
    end_draw = n - a              
    for i in range(start_draw, end_draw):
        B[i] = A[i]
        used[A[i]] = True

 
    cur = n
    for i in range(0, b):
        while used[cur]:
            cur -= 1
        B[i] = cur
        used[cur] = True
        cur -= 1

   
    cur = 1
    for i in range(n - a, n):
        while used[cur]:
            cur += 1
        B[i] = cur
        used[cur] = True
        cur += 1

 
    aa, bb = a, b
    for i in range(n):
        if A[i] > B[i]:
            aa -= 1
        elif A[i] < B[i]:
            bb -= 1
    if aa != 0 or bb != 0:
        print("NO")
        return

    print("YES")
    print(*A)
    print(*B)



t = int(input().strip())
for _ in range(t):
    n,a,b = map(int, input().split())
    solve_one(n,a,b)
