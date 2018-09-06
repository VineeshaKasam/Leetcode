
def romanToInt(s):
    roman = {"I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000 }

    len1 = len(s)
    len2 = len(s)-1
    i=0
    ans = 0
    while i<len2:
        if roman[s[i]] < roman[s[i+1]]:
            ans += roman[s[i+1]] - roman[s[i]]
            i+=2
        else:
            ans+=roman[s[i]]
            i+=1

    if i<len1:
        ans+=roman[s[len2]]

    return ans


print romanToInt("VIII")
print romanToInt("MCMXCIV")


