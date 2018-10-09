'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        index = 0
        path = ""
        result = []
        self.dfs(s, index, path, result)

        return result


    def dfs(self, s, index, path, result):
        if index == 4:
            if len(s) == 0:
                result.append(path[:-1])
            return

        for i in range(1, 4):
            if i <= len(s):

                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", result)

                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", result)

                elif i == 3 and int(s[:3]) <= 255 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", result)