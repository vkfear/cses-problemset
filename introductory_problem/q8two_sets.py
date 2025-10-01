def two_sets(n):
    total = n * (n + 1) // 2
    

    if total % 2 != 0:
        print("NO")
        return
    
    print("YES")
    target = total // 2
    set1, set2 = [], []
    

    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)
    

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)

if __name__ == "__main__":

    n = int(input().strip())
    two_sets(n)
