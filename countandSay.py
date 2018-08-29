'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
'''

def countAndSay(n):

    s = '1'
    for _ in range(n - 1):
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
    return s

print(countAndSay(5))