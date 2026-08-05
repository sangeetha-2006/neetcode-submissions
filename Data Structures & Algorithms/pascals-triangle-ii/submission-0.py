class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[]
        for i in range(rowIndex + 1):
            curr=[]
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(arr[i-1][j-1] + arr[i-1][j])
            arr.append(curr)
        return arr[rowIndex]



        