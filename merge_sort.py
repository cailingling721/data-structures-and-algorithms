# coding:utf-8
def merge_sort(alist):
	"""归并算法"""
	n = len(alist)
	if n <= 1:
		return alist
	mid = n//2
	# left和right采用归并排序后形成的有序的新的列表
	left = merge_sort(alist[:mid])
	right = merge_sort(alist[mid:])
	# 将两个有序的子序列合并为一个新的整体
	# merge(left, right)
	left_pointer, right_pointer = 0, 0
	result = []
	while left_pointer < len(left) and right_pointer < len(right):
		if left[left_pointer] <= right[right_pointer]: # 加上等号就是稳定排序
			result.append(left[left_pointer])
			left_pointer += 1
		elif:
			result.append(right[right_pointer])
			right_pointer += 1
	# 走出循环说明有一个已经走到头了,只需要将剩下的某一个list剩下的部分append在result中；空列表也是可以追加的
	result += left[left_pointer:]
	result += right[right_pointer:]
	return result

if __name__ = "__main__":
	li = [34,56,78,23,14,56,23,789,90]
	print(li)
	sorted_li = merge_sort(li)
	print(li)
	print(sorted_li)
  
  # 合并排序的具体过程，因为包含递归，所以列出来具体的排序过程
  left_li = merge_sort [34,56,78,23]
	left_li = merge_sort [34,56]
		left_li = merge_sort([34])
			return [34]
		left_li = [34]
		right_li = merge_sort([56])
			return [56]
		right_li = [56]
		result = [34,56]
		return result
	left_li = [34,56]
	right_li = merge_sort([78, 23])
		left_li = merge_sort([78])
			return [78]
		left_li = [78]
		right_li = merge_sort([23])
			return [23]
		right_li = [23]
		result = [23, 78]
		return result
	right_li = [23, 78]
	result = [23,34,56,78]
	return result
left_li = [23,34,56,78]
  
  
  
