class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle=[]

        for i in range(numRows):

            rows=[None for _ in range(i+1)]

            rows[0], rows[-1]=1, 1

            for j in range(1, len(rows)-1):

                rows[j]=triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(rows)

        return triangle


        