# coding:utf-8
class Node(object):
	def __init__(self, item):
		self.elem = item
		self.lchild = None
		self.rchild = None

class Tree(object):
	def __init__(self):
		self.root = None

	def add(self, item):
		node = Node(item)
		queue = [self.root]
		while queue: # 只要不为空就执行
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				queue.append(cur_node.rchild)

# 二叉树的遍历，主要包括广度遍历，以及深度遍历（先序遍历，中序遍历以及后序遍历）
def breadth_travel(self):
	"""广度遍历，横向遍历，层次遍历，同上面的add的思路"""
	if  self.root is None:
		return
	queue = [self.root]
	while queue:
		cur_node = queue.pop(0)
		print(cur_node.elem)
		if cur_node.lchild is not None:
			queue.append(cur_node.lchild)
		if cur_node.rchild is not None:
			queue.append(cur_node.rchild)
      
def preorder(self, node):
	"""先序遍历"""
	if node == None:
		return
	print(node.elem, end = " ") # 根节点
	self.preorder(node.lchild) # 左子树
	self.preorder(node.rchild) # 右子树

def inorder(self, node):
	"""中序遍历"""
	if node == None:
		return
	self.inorder(node.lchild) # 左子树
	print(node.elem, end = " ") # 根节点
	self.inorder(node.rchild) # 右子树

def postorder(self, node):
	"""后序遍历"""
	if node == None:
		return
	self.postorder(node.lchild) # 左子树
	self.postorder(node.rchild) # 右子树
	print(node.elem, end = " ") # 根节点

if __name__ = "__main__":
	tree = Tree()
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
  tree.breadth_travel()
	tree.preorder(tree.root)
	print("")
	tree.inorder(tree.root)
	print("")
	tree.postorder(tree.root)








