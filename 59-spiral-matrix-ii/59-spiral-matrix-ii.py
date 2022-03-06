class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[None for _ in range(n)] for _ in range(n)]
    
        def recur(top, bottom, left, right, val):
            if top > bottom or left > right:
                return
            
            # there's one cell left
            if top == bottom and left == right:
                output[top][left] = val
                return
                
                    
            # top part
            for col in range(left, right+1):
                output[top][col] = val
                val += 1
            
            # right part
            for row in range(top+1, bottom):
                output[row][right] = val
                val += 1
            
            # bottom part (reverse)
            for col in range(right, left-1, -1):
                output[bottom][col] = val
                val += 1
                
            # left part (reverse)
            for row in range(bottom-1, top, -1):
                output[row][left] = val
                val += 1
                
            recur(top+1, bottom-1, left+1, right-1, val)

        recur(0, n-1, 0, n-1, 1)
        return output
            