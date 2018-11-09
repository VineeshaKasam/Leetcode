class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # i = len(s)-1
        # res = ""
        # while i>=0:
        #     res+=s[i]
        #     i-=1
        #
        # return res

        len = len(s)
        res = list(s)
        for i in range(len / 2):
            res[len- 1], res[i] = s[i], s[len - 1]
            len -= 1
        return ''.join(res)

        # return s[::-1]