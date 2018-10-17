'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        def constructdict(words):
            mydict = {}
            for word in words:
                for i in range(0, len(word)):
                    key = word[:i] + "_" + word[i + 1:]
                    mydict[key] = mydict.get(key, []) + [word]

            return mydict

        def bfs(start, end, mydict):
            from collections import deque
            queue, visited = deque([(start, 1)]), set()

            while queue:
                popword, steps = queue.popleft()

                print popword, steps

                if popword not in visited:
                    visited.add(popword)

                    # print popword, end
                    if popword == end:
                        return steps

                    for i in range(0, len(popword)):
                        key = popword[:i] + "_" + popword[i + 1:]

                        adj_words = mydict.get(key, [])

                        for k in range(0, len(adj_words)):
                            if adj_words[k] not in visited:
                                queue.append((adj_words[k], steps + 1))
            return 0

        mydict = constructdict(wordList)
        return bfs(beginWord, endWord, mydict)