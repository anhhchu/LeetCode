class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        freq_bucket = [ [] for i in range(len(nums) + 1) ]
        
        # populate count
        # count freq the old-fashioned way
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        for num, c in count.items():
            freq_bucket[c].append(num)
           
        # get result from freq_bucket
        res = []
        # loop reversedly
        for i in range(len(freq_bucket) - 1, 0 , -1): 
            for num in freq_bucket[i]: # empty or not
                res.append(num)
                if len(res) == k:
                    return res
                
            
        