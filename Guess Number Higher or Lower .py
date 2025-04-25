def guessNumber(m: int) -> int:
    low, high = 1, m
    
    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)
        
        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1
