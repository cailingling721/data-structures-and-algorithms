def quick_sort(alist, first, last):
	if fisrt >= last: # 代表子列表只有一个元素
		return
	mid_value = alist[first]
	low = first
	high = last

	while low < high:
		# high左移或者low右移
		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high] # 赋值的过程

		while low < high and alist[low] < mid_value:
			low += 1
		alist[high] = alist[low]
	# 退出循环时，low = high
	alist[low] = mid_value
	# 对low左边的执行快速排序，递归调用
	quick_sort(alist, first, low -1)
	# 对low右边的执行快速排序，递归调用
	quick_sort(alist, low+1, last)

if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	quick_sort(li, 0, n-1)
	print(li)
