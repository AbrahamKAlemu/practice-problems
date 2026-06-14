from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.count_pts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.count_pts[tuple(point)] += 1
        self.pts.append(tuple(point))

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for cx, cy in self.pts:
            if x == cx or y == cy or abs(x - cx) != abs(y - cy):
                continue
            res += self.count_pts[cx, y] * self.count_pts[x, cy]
        return res
