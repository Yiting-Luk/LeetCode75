from bisect import bisect_left
def successfulPairs(spells, potions, success):
    potions.sort()
    m = len(potions)
    result = []

    for spell in spells:
        required_strength = (success + spell - 1) // spell # spell x potion > success 
        # 直接使用除法会出现浮点数，使用小技巧（+ spell - 1）实现向上取整， -1是为了避免整数倍时不向上取整
        index = bisect_left(potions, required_strength) #bisect_left用于在有序list中查找某个插入值的插入点，仍然保持序列的有序性
        result.append(m - index)
    return result

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))