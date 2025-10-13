def generate_permutations(s):
    
    if len(s) == 1:
        return [s]

    permutations = set()  

    for i in range(len(s)):
        
        ch = s[i]
       
        remaining = s[:i] + s[i+1:]

        for perm in generate_permutations(remaining):
            permutations.add(ch + perm)

    return list(permutations)

s =input()
result = generate_permutations(s)

for p in result:
    print(p)

print("Total permutations:", len(result))
