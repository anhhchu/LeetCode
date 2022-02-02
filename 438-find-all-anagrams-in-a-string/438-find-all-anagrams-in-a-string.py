from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n_p, n_s = len(p), len(s)
        
        if n_s < n_p:
            return []
        
        counter_p = Counter(p)
        counter_s = Counter()
        
        output = []
        for i in range(n_s):
            # add letter in the right
            counter_s[s[i]] += 1
            # remove letter in the left
            if i >= n_p:
                counter_s[s[i - n_p]] -= 1
                if counter_s[s[i - n_p]] == 0:
                    counter_s.pop(s[i - n_p])
            #print(counter_s)    
            if counter_s == counter_p:
                output.append(i - n_p + 1)
                
        return output
            