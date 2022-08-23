from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N)
        counter = Counter(nums)
        # O(NlogN)
        sortedCounter = [k for k, v in sorted(counter.items(), key = lambda item : -item[1] )]
        return sortedCounter[:k]