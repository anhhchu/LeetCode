from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for string in strs:
            sortedstring = ''.join(sorted(string))
            hm[sortedstring].append(string)
            
        return hm.values()
            