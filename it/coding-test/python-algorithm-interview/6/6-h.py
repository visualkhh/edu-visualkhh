class Solution:
    def longestPalindrome(self, s: str) -> str:
        for idx, it in enumerate(s):
            # print(idx, it);
            start = idx;
            result = '';
            for i in range(idx, len(s)):
                start -= 1;
                start = max(0, start);
                ms = s[start:i]
                msr = ''.reversed(ms)
                print(ms, msr);
                result = ms if ms == msr and len(ms) > len(result) else result;
                # print(i, s[i]);
        return result

if __name__ == '__main__':
    print(Solution().longestPalindrome('babsaokdfjuidslkjabbbbbaad'))