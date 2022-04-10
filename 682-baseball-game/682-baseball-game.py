class Solution:
    def calPoints(self, ops: List[str]) -> int:
        #print("5".isnumeric())
        scores = []
        for item in ops:
            print(item, scores)
            if item.isnumeric() or item[0] == '-':
                scores.append(int(item))
            elif item == 'C':
                scores.pop()
            elif item == 'D':
                scores.append(2*scores[-1])
            elif item == '+':
                scores.append(scores[-1]+scores[-2])
            
        return sum(scores)