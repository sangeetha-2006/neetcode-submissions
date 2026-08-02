class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = []

        for row in matrix:
            arr.extend(row)

        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] == target:
                return True

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False