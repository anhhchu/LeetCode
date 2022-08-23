class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Identity the delimeter that is outside of ASCII 256
        d = chr(257)
        
        # prefix lenght and d in front of the string
        res = ""
        for string in strs:
            res += str(len(string)) + d + string
            
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
        
            j = i
            while s[j] != chr(257):
                j += 1
            length = int(s[i:j])
            string = s[j + 1 : j + 1 + length]
            res.append(string)
            i = j + 1 + length
            
        return res
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))