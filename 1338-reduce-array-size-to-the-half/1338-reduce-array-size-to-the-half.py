from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        values = sorted(counter.values(), reverse=True)
        sum = 0; m = len(arr)/2; i = -1
        while sum < m:
            i += 1
            sum += values[i]
            
        return i+1
            