def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2


    array_sum = sum(nums)

    missing_number = total_sum - array_sum

    return missing_number


if __name__ == "__main__":
    n=6
    numbers = [1, 2, 4, 5, 6]
    print(find_missing_number(numbers))