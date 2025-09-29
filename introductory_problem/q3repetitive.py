def repetition(s):

    count= 1
    max_count=1

    for i in range(1, len(s)):

        if s[i] == s[i-1]:
            
            count+=1

        else :
            count =1
        
        if count > max_count:
            max_count = count
    
    return max_count

if __name__ == "__main__":
    s=str(input())

    print(repetition(s))