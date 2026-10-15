class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        stack = [(0, target, [])]
        while stack:
            start, remaining, path = stack.pop()
            if remaining == 0:
                result.append(path)
                continue
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break
                stack.append((i, remaining - candidate, path + [candidate]))
        return result
