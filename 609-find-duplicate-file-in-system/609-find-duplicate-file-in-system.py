from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        files_count = 0
        for path in paths: # O(N) -> 10**4
            files = path.split(" ") # O(3000)
            path = files[0]  
            for i in range(1, len(files)): # O(files)
                files_count += 1
                f = files[i]
                file, content = f.split("(")
                contents[content[:-1]].append(path + "/" + file)
                
        return [lst for lst in contents.values() if len(lst) > 1]
        