def letterCombinations(digits):
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if not digits:
        return []
    
    result = []
    def backtrack(index, currentCombination):
        if index == len(digits):
            result.append(currentCombination)
            return
        letters = phone_map[digits[index]]
        for letter in letters:
            backtrack(index + 1, currentCombination + letter)
            
    backtrack(0, "") # 第一次递归调用
    return result

digits = "23"
print(letterCombinations(digits))
