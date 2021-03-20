class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = collections.Counter(nums)
        result = []

        sorted_items = sorted(counter.items(), key=lambda x : -x[1])

        return [x[0] for x in sorted_items[:k]]
