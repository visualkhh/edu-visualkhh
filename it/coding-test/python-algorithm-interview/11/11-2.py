from typing import List

#주연경
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)
        extended_nums = nums * size

        answer = [1] * (size+1)
        for i, n in enumerate(extended_nums) :
            answer[i%(size+1)] *= extended_nums[i]

        return answer[1:]

        '''
        double_nums = nums * 2
        size = len(nums)
        
        temp = []
        for i in range(size-1) :
            temp.extend(double_nums[i+1:i+size+1])
            
        answer = [1] * size
        for i, n in enumerate(temp) :
            answer[i%size] *= n
        
        return answer
        '''
