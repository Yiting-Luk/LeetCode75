def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    
    # function to calculate the total hours needed at speed k
    def hours_needed(k):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k
        return total_hours
    
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h: # speed is too high
            right = mid
        else:
            left = mid + 1
    return left
print(minEatingSpeed([3,6,7,11], 8)) 