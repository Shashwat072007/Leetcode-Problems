class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}
        for winner,losser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[losser] = losses.get(losser,0)+1
        z = []
        o = []
        for p,c in losses.items():
            if c == 0:
                z.append(p)
            elif c == 1:
                o.append(p)
        z.sort()
        o.sort()
        return [z,o]