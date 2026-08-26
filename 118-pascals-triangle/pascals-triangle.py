class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for _ in range(1, numRows):
            prev = result[-1]

            left = [0] + prev
            right = prev + [0]

            row = []

            for i in range(len(left)):
                row.append(left[i] + right[i])

            result.append(row)

        return result
