from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        
        # check row
        for r in range(9):
            hm = set()
            for c in range(9):
                    
                if board[r][c] in hm:
                    #print(r, hm)
                    return False
                elif board[r][c] != ".":
                    hm.add(board[r][c])
                
                br, bc = r//3, c//3 # find index for box
                if (br, bc) in boxes and board[r][c] in boxes.get((br, bc)):
                    #print((br, bc), boxes.get((br, bc)))
                    return False
                elif board[r][c] != ".":
                        boxes[(br, bc)].add(board[r][c])

                        
        # check col
        for c in range(9):
            hm = set()
            for r in range(9):
                if board[r][c] in hm:
                    #print(c, hm)
                    return False
                elif board[r][c] != ".":
                    hm.add(board[r][c])

                        
        return True