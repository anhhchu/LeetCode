# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right)//2
            # if mid == right:
            #     return mid   
            if isBadVersion(mid) == True: 
                if mid == left or isBadVersion(mid-1) == False:
                    return mid
                else:
                    right = mid - 1
            
            elif isBadVersion(mid) == False: # look right
                left = mid + 1
            
                
                