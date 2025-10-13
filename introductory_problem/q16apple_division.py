n = int(input())
weights = list(map(int, input().split()))

total = sum(weights)
min_diff = float('inf')


for mask in range(1 << n):   
    group1_sum = 0
    for i in range(n):
        if mask & (1 << i): 
            group1_sum += weights[i]
    group2_sum = total - group1_sum
    min_diff = min(min_diff, abs(group1_sum - group2_sum))

print(min_diff)
