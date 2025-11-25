class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]

        for i in range(rowIndex+1):
            res.append([1]*(i+1))
        
        if rowIndex<2:
            return res[rowIndex]

        for i in range(2,rowIndex+1):
            for j in range(1,i):
                res[i][j]=res[i-1][j]+res[i-1][j-1]
        
        return res[rowIndex]