class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dd = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dd[tuple(count)].append(s)
        return dd.values()
        # for s in strs:
        #     dd[tuple(sorted(s))].append(s)
        # return dd.values()
        
    