import re
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for it in logs:
            # print(it)
            # s = re.search('^[a-z]+[0-9][\s](.*)', it).group(0)
            # s = re.search('(?<=^[a-z][0-9][\s]).*', it).group(0)
            s = re.match(r'([a-z]+[0-9][\s])(.*)', it, re.M | re.I)
            # s = re.sub('^. [^a-z0-9]', '', it) # 정규식으로 불필요한 문자 필터링
            print(s.group(1))
            # print(s.group(2))
            print(re.sub('[^a-z0-9]', '', s.group(2)))
            if re.sub('[^a-z0-9]', '', s.group(2)).isalnum():
                digits.append(it)
            else:
                letters.append(it)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


if __name__ == '__main__':
    palindrome = Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    print(palindrome)
