class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        word="ABCESEEEFS"""
        def dfs(r, c, i, seen):
            if i == len(word):
                return True
            if (r < 0 or r == len(board) or
                    c < 0 or c == len(board[r]) or
                    board[r][c] != word[i] or
                    (r, c) in seen):
                return False

            seen.add((r, c))
            
            res = (dfs(r + 1, c, i + 1, seen) or dfs(r - 1, c, i + 1, seen) or 
                dfs(r, c + 1, i + 1, seen) or dfs(r, c - 1, i + 1, seen))
            
            seen.remove((r, c))
            return res 

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0] and dfs(r, c, 0, set()):
                    return True
        return False

        