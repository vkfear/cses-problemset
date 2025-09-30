def beautiful_order(N):
    
    if N == 2 or N == 3 :
        print("NO SOLUTION")
        return
    
    for i in range(2,N+1,2):
        print(i)

    for i in range(1,N+1,2):
        print(i)

if __name__ == "__main__":

    N = int(input())

    beautiful_order(N)