#岛屿数量：https://leetcode-cn.com/problems/number-of-islands/
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
#解题：循环遍历每一个节点，把为1的数值置为0，全部遍历后就是最后的数据
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(grid,i,j):
            #terminator
            if not 0 <= i <len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':return
            grid[i][j]='0'
            DFS(grid,i+1,j)
            DFS(grid,i,j+1)
            DFS(grid,i-1,j)
            DFS(grid,i,j-1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    DFS(grid,i,j)
                    count+=1
        return count
