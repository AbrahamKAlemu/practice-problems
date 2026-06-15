class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tag = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if tag[c] != t:
                    return False
        return len(stack) == 0
        