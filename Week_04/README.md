学习笔记：
1、搜索一般在没有加入任何智能的情况下，绝大多数情况下处理的都是暴力搜索，很多的搜索就是把所有的结点全部遍历一遍，找到你要的结果。对于节点的访问顺序不同可以分为深度优先(depth first search)和广度优先(breadth first search)；还有例如优先级优先搜索，一般称为启发式搜，一般用在推荐算法和高级的搜索算法里。  深度优先搜索算法可以用递归进行求解：

#dfs示例：
def dfs(node):
    if node in visited:
    #already visited
        return
    visited.add(node)
    #process current node
    #...#logic here
    dfs(node.left)
    dfs(node.right)
    
#dfs-递归写法
visited=set()
def dfs(node,vistied):
    if node in visited: #terminator
        return
    visited.add(node)
    #process current node
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visited)
  也可以用非递归的写法进行：

#dfs-非递归写法(用栈来维护)
def DFS(self,tree):
    if tree.root is None:
        return []
    visited,stack=[],[tree.root]
    while stack:
        node=stack.pop()
        visited.add(node)
        process(node)
        nodes=generate_related_nodes(node)
        stack.push(nodes)
        
  实际中的例子如下

#给你一个二叉树，请你返回其按 层序遍历 得到的节点值，该问题也可以使用广度搜索进行求解
class Solution(object):
    def levelOrder(self, root):
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root: 
            return
        if len(res) == level: 
            res.append([])
        res[level].append(root.val)
        if root.left: 
            self.level(root.left, level + 1, res)
        if root.right: 
            self.level(root.right, level + 1, res)
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
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
        
2、 广度优先搜索主要是用的队列的方式，第一层遍历后再第二层遍历，依次往下进行遍历。深度优先搜索用递归程序能帮忙维护一个栈，但是广度优先搜索就没得帮忙维护队列，所以只能自己维护一个队列：

#BFS
def BFS(graph,start，end):
    queue=[]
    queue.append([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        visited.add(node)
        process(node)
        nodes=generate_related-nodes(node)
        queue.push(nodes)
    #other processing work
#如果不需要确定当前遍历到了哪一层，模板如下
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)
#如果需要确定当前遍历到了哪一层
level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++
  实际中的例子如下

#给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
3、贪心算法是一种在每一步的选择中都采取在当前状态下是最好或者最优的选择，这样导致最终的结果是全局最好或最优的算法。

  贪心算法与动态规划的区别在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的计算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心：当下做局部最优判断
回溯：能够回退
动态规划：最优判断+回退
  贪心算法可以解决部分的最优解问题，例如：求图中的最小生成树、求哈夫曼编码等。最重要的是怎么确定这个问题适合用贪心算法来求解，举例如下：

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易
#（多次买卖一支股票）。 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 示例 1: 
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）
# 的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）
# 的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                total+=prices[i+1]-prices[i]
        return total
  上面由于局部最优解就是全局的最优解，故可以使用贪心算法，还有一些问题是需要通过从特殊得角度去求解该问题才能使用贪心算法，例如以下问题：

# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        if nums is None:
            return False
        for i in range(last,1,-1):
            if nums[i]+i>=last:
                last=i
            return last==0