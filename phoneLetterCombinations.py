'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.
'''

def letterCombinations(digits):

    digits_dict = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                   "9": "wxyz"}

    if digits == "":
        return []
    result = [""]
    for i in digits:
        newresult = []
        for char in digits_dict[i]:
            for str_val in result:
                newresult.append(str_val + char)
        result = newresult

    return result