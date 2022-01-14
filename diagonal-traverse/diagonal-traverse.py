class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        nums_rows = len(mat)
        nums_cols = len(mat[0])
        
        nums_diag = [[] for _ in range(nums_rows + nums_cols - 1)]
        
        for i in range(nums_rows):
            for j in range(nums_cols):
                nums_diag[i+j].append(mat[i][j])
        
        res = nums_diag[0]
        
        for x in range(1, len(nums_diag)):
            if x%2 == 1:
                res.extend(nums_diag[x])
            else:
                res.extend(reversed(nums_diag[x]))
        return res