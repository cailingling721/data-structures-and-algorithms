# coding:utf-8

#（1）递归实现：
def binary_search(alist, item):
	"""二分查找，递归"""
	n = len(alist)
	if n > 0:		
		mid = n//2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			return binary_search(alist[:mid])
		elif item < alist[mid]:
			return binary_search(alist[mid+1:])
	return False
#（2）非递归实现
def binary_search(alist, item):
	"""二分查找，非递归"""
	n = len(alist)
	first = 0
	last = n-1
	while fist <= last:
		mid = (first + last)//2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			last = mid -1
		else:
			first = mid + 1
	return False

if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	binary_search_1(li, 34)
	binary_search_1(li, 3)
  binary_search_2(li, 34)
  binary_search_2(li, 3)
	print(li)
  
  
  
  
