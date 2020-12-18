# 현하
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower()) # 정규식으로 불필요한 문자 필터링
        print(s)
        length = len(s)
        for i in range(0, int(length/2)):
            head = s[i:i + 1]
            tail = s[length - (i + 1):length - i]
            if head != tail:
                return False
            print(head + ' , ' +tail)
        return True

if __name__ == '__main__':
    palindrome = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(palindrome)
