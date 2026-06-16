class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + '#' + s
        
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        code = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            code.append(s[i: i + num])
            i += num
        return code