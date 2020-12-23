import re
from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = re.sub('[^a-z0-9]', '', s.lower())
        length = len(s)
        halfLength = length // 2
        header = s[:halfLength]
        tail = s[halfLength:length]
        header = header[::-1]
        a,mod = divmod(length, 2)
        grade = mod > 0 and 1 or 0

        print('header', header, 'tail', tail, 'grade', grade, 'a', a)
        s = []
        # for start in range(len(header)):
        #     useHeader = header[start:]
        #     for i in range(len(useHeader), 0, -1):
        #         print(useHeader[:i], tail[:i])
        #         if useHeader[grade:i] == tail[:1]:
        #             s.append(useHeader[grade::-1] + useHeader[grade])
        #         elif len(useHeader[grade:i]) <= 1:
        #             s.append(useHeader[grade:i])
        #
        # print('-->',s)
        headerFirst = len(s) > 0 and sorted(s, key=len)[-1] or ''

        s.clear()
        for start in range(len(tail)):
            useTail = tail[start:]
            print('useTail', useTail)
            for i in range(len(useTail), 0, -1):
                print(header[:i], useTail[:i])
                if header[:i] == useTail[:i]:
                    s.append(useTail[::-1])
                elif len(useTail[:i]) <=1:
                    s.append(useTail[:i])


        tailFirst =  len(s) > 0 and sorted(s, key=len)[-1] or ''

        return len(headerFirst) < len(tailFirst) and tailFirst or headerFirst

if __name__ == '__main__':
    palindrome = Solution().longestPalindrome('ccc')
    # palindrome = Solution().longestPalindrome('cbbd')
    print(palindrome)
