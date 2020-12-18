# 김동억
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArray = [c.lower() for c in s if c.isalnum()]
        chkIndex = len(sArray)//2
        for idx, c in enumerate(sArray):
            if idx >= chkIndex:
                return True
            if c != sArray[-idx-1]:
                return False
        return True

if __name__ == '__main__':
    palindrome = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(palindrome)
