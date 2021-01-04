# 주연경
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = dict()
        for i, num in enumerate(nums) :
            if not num in dic.keys() :
                dic[num] = []
            dic[num].append(i)


        for n1 in dic.keys() :
            n2 = target - n1
            if n2 in dic.keys() :
                if n1 == n2 :
                    if len(dic[n1]) >= 2 :
                        return [dic[n1][0], dic[n1][1]]
                    else :
                        continue
                else :
                    return [dic[n1][0], dic[n2][0]]
