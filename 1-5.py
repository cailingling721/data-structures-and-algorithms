## 剑指offer题目1: 输入一个链表，返回一个反序的链表 ##
题目：输入一个链表，返回一个反序的链表
思路：通常，这种情况下，我们不希望修改原链表的结构。返回一个反序的链表，这就是经典的“后进先出”，我们可以使用栈实现这种顺序。每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，给一个新的链表结构，这样链表就实现了反转。
对于python来讲，不用如此麻烦，我们可以直接使用列表的插入方法，每次插入数据，只插入在首位。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result

## 剑指offer 题目2:链表中倒数第k个节点  ##
题目：输入一个链表，输出该链表中倒数第k个结点。
思路：我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，当第一个（走在前面的）指针到达链表的尾结点时，第二个指针（走在后面的）指针正好是倒数第k个结点。
## 方法1 ：方法与C++一致 ##
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        phead = head
        pbehind = head
        for i in range(k-1):
            if phead.next == None:
                return None
            else:
                phead = phead.next
        while phead.next != None:
            phead = phead.next
            pbehind = pbehind.next
        return pbehind
## 方法2 ：使用列表，但是开辟新空间了，没有上面的方法好 ##
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < k or k < 1:
            return None
        return l[-k]

## 剑指offer 题目3：反转链表 ##
题目：输入一个链表，反转链表后，输出链表的所有元素。
思路：这个很简单，我们使用三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点。在遍历的时候，做当前结点的尾结点和前一个结点的替换。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

## 剑指offer 题目4: 合并两个排序的链表 ##
题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
思路：
	先判断输入的链表是否为空的指针。
	如果第一个链表为空，则直接返回第二个链表；
	如果第二个链表为空，则直接返回第一个链表。
	如果两个链表都是空链表，合并的结果是得到一个空链表。
	两个链表都是排序好的，我们只需要从头遍历链表，判断当前指针，哪个链表中的值小，即赋给合并链表指针即可。
	使用递归就可以轻松实现。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead

## 剑指offer 题目5: 复杂链表的复制 ##
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
思路：
	大部分人首先想到的可能是先复制复杂指针的label和next，然后再查找random并更新。查找random又分为两种，一种是每次都从头查找，时间复杂度为O(n^2)；
	另一种是空间换时间，复制label和next的同时建立一个hash表来存放新旧复杂指针的对应关系，所以后续只需一步就能找到random，算法时间复杂度为O(n)。
	我们这里将复杂链表的复制过程分解为三个步骤。在写代码的时候我们每一步定义一个函数，这样每个函数完成一个功能，整个过程的逻辑也就非常清晰明了了。
	我们这里采用三步：
	第一步：复制复杂指针的label和next。但是这次我们把复制的结点跟在元结点后面，而不是直接创建新的链表；
	第二步：设置复制出来的结点的random。因为新旧结点是前后对应关系，所以也是一步就能找到random；
	第三步：拆分链表。奇数是原链表，偶数是复制的链表。
	有图思路更清晰：
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
	def Clone(self, pHead):
	    if not pHead:
	        return None
	    cloneHead = RandomListNode(pHead.label)
	    cloneHead.random = pHead.random
	    cloneHead.next = self.Clone(pHead.next)
	    return cloneHead
思路：一开始都没看懂题，后来看了大家的评论才知道复杂链表的复制是咋回事．思路就是先遍历链表，把next的节点都复制好，然后再查看每个节点的random指向哪里了，就让新链表的random也指向哪里
class Solution:
    # 返回 RandomListNode
    def CloneNext(self,root):
        if root:
            cHead = RandomListNode(root.label)
            cHead.next = self.CloneNext(root.next)
            return cHead
    def Clone(self, pHead):
        # write code here
        if pHead:
            cHead = self.CloneNext(pHead)
            pList = []
            cList = []
            while pHead:
                pList.append(pHead)
                cList.append(cHead)
                pHead = pHead.next
                cHead = cHead.next
            for i in range(len(pList)):
                if pList[i].random:
                    index = pList.index(pList[i].random)
                    cList[i].random = cList[index]
            return cList[0]
