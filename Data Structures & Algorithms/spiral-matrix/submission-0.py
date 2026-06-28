class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L, R = 0, len(matrix[0]) - 1
        T, B = 0, len(matrix) - 1
        res = []

        while L <= R and T <= B:
            for l in range(L, R + 1):
                res.append(matrix[T][l])
            T += 1
            for b in range(T, B + 1):
                res.append(matrix[b][R])
            R -= 1

            if not (L <= R and T <= B):
                break

            for r in range(R, L - 1, -1):
                res.append(matrix[B][r])
            B -= 1
            for t in range(B, T - 1, -1):
                res.append(matrix[t][L])
            L += 1
        return res
        