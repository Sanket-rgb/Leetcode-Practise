class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dd = collections.defaultdict(list)
        
        for s in strs:
            dd[tuple(sorted(s))].append(s)
        return dd.values()
        
    