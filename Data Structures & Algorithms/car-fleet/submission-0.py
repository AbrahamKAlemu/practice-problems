import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(zip(position, speed), reverse=True)
        last_time = -1.0
        res = 0

        for i in range(len(fleets)):
            cT = (target - fleets[i][0]) / fleets[i][1]
            if cT > last_time:
                res += 1
                last_time = cT
        return res
        