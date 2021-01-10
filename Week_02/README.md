学习笔记：
本周学习了哈希、映射集合和树、二叉树、二叉搜索树，堆和二叉堆，图等。
了解到了堆有多种解法，且二叉堆是其中比较简单的方法，但是时间复杂度相
对被的方法较高，还了解到二叉搜索树插入和查询都为logn的，根节点一定
大于左节点，一定小于右节点。二叉堆是一种完全二叉树。了解了链表和树、
图的关系

#前序遍历
def preorder(self,root):
    if root:
    self.path.append(root.val)
    self.preorder(root.left)
    self.preorder(root.right)
#中序遍历
def preorder(self,root):
    if root:
    self.preorder(root.left)
    self.path.append(root.val)
    self.preorder(root.right)
#后续遍历
def preorder(self,root):
    if root:
    self.preorder(root.left)
    self.preorder(root.right)
    self.path.append(root.val)