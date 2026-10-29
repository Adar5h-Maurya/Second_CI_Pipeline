def find_missing_number(numbers, n):
    missing = n

    for i in range(n):
        missing ^= i
        missing ^= numbers[i] if i < len(numbers) else 0

    return missing