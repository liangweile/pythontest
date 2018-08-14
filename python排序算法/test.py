#冒泡排序
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]

#直接排序
def select_sort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)-1):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

#插入排序
def insert_sort(array):
    for i in range(1, len(array)-1):
        min = array[i]
        j = i-1
