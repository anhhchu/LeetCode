class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removes = set()
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if not stack:
                    removes.add(i)
                else:
                    stack.pop()
        
        while stack:
            removes.add(stack.pop())
            
        output = ""
        for i, char in enumerate(s):
            if i not in removes:
                output += char
                
        return output
            
        
            
                    
                
                