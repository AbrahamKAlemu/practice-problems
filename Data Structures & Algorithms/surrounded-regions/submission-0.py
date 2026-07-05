class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        seen = set()
        def dfs(r, c):
            if (r < 0 or r == len(board) or 
                    c < 0 or c == len(board[r]) or 
                    board[r][c] == "X" or (r, c) in seen):
                return 
            board[r][c] = "M"
            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r == 0 or r == len(board) - 1 or
                        c == 0 or c == len(board[r]) - 1):
                    if board[r][c] == "O":
                        dfs(r, c)
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "M":
                    board[r][c] = "O"

