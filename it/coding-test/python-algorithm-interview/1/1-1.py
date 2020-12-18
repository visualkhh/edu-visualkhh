# 김태형
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ori_s = ''

        for i in range(len(s)):
            if s[i].isalnum() == True:
                ori_s += s[i]

        ori_s = ori_s.lower()
        list_s = list(ori_s)
        list_s.reverse()
        new_s = ''.join(list_s)

        if ori_s == new_s:
            return True
        else:
            return False

if __name__ == '__main__':
    palindrome = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(palindrome)
