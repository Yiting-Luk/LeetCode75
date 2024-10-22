def guess(num: int) -> int:
    if num < pick:
        return 1
    if num > pick:
        return -1
    else:
        return 0
    
def guessNumber(n: int) -> int: # -> int 函数返回类型提示
    low, high = 1, n
    
    while low <= high:
        mid = (low + high) // 2
        result = guess(mid)
        
        if result == 0:
            return mid  # This is the number we picked.
        elif result == -1:
            high = mid - 1  # The picked number is lower than mid.
        else:
            low = mid + 1  # The picked number is higher than mid.

n = 10
pick = 6
result = guessNumber(n)
print(result)