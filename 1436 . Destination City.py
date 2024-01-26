class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set([paths[i][0] for i in range(len(paths))])
        destinations = set([paths[i][1] for i in range(len(paths))])
        res = (destinations - sources).pop()
        return res
