from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print('======',nums)
        r = []
        for i in range(len(nums) - 1):
            # print(nums[i], nums[i+1:])
            ts = nums[i+1:]
            # ts = nums[:i] + nums[i+1:]
            print(ts)
            for j in range(len(ts) - 1):
                # print('-> ', ts[j], ts[j+1:])
                tts = ts[j+1:]
                for k in range(len(tts) - 1):
                    # print('-> -> ', tts[k], tts[k+1:])
                    if nums[i] + ts[j] + tts[k] == 0:
                        r.append(sorted([nums[i], ts[j], tts[k]]))

        return r


if __name__ == '__main__':
    palindrome = Solution().threeSum([-1,0,1,2,-1,-4])
    print('result->', palindrome)

