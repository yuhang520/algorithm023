# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
  ##首先需要拿出其中的一个跟第二个list中的进行比较
  ##再拿剩下的进行比较，分2种情况
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 审题：
        #     1、链表合并问题
        #     2、且都是有序的，合并后也需要有序的
        #
        # 可用解法：
        #     1、暴力循环去插入
        #     2、递归的方法
        if not l1:     #如果l1为空则直接返回l2,相反也一样
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2


# leetcode submit region end(Prohibit modification and deletion)




