#从前序与中序遍历序列构造二叉树：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#定义树
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def buildTree(self,perorder:List[int]，inorder:List[int]):
    #解体：根据前序和终序遍历可以构造相应的二叉树,使用递归求解
    #终止条件为前序数组为none，或中序为NONE
        if not (perorder and inorder):
            return None
        #前序的第一个为根结点
        root=TreeNode(perorder[0])
        #查找出中序的根结点的index
        mid_index=inorder.index(perorder[0])
        root.left=self.buildTree(perorder[1:mid_index],inorder[:mid_index])
        root.right=self.buildTree(perorder[mid_index+1:],inorder[mid_index+1:])
        return root



