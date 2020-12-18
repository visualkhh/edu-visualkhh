# 주연경
class Solution:
    def isPalindrome(self, s: str) -> bool:

        upper_s = s.upper()

        re_list = list(filter(lambda x : x.isalnum(), upper_s))
        return re_list[:] == re_list[::-1]

if __name__ == '__main__':
    palindrome = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(palindrome)
