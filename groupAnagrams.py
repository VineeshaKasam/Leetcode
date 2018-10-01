'''
Given an array of strings, group anagrams together.
'''

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mydict = {}

    for word in strs:
        key = tuple(sorted(word))
        mydict[key] = mydict.get(key, []) + [word]

    return mydict.values()