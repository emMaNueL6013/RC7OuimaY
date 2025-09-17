# 代码生成时间: 2025-09-17 20:55:01
#!/usr/bin/env python

# 导入bottle框架
from bottle import route, run

# 排序算法实现
def bubble_sort(arr):
    # 冒泡排序算法，对数组进行排序
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    # 快速排序算法，对数组进行排序
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Bottle应用路由
@route('/sort', method='GET')
def sort_algorithm():
    # 从查询参数获取数组
    arr = request.query.arr
    if not arr:
        return {"error": "No array provided"}
    try:
        arr = eval(arr)
        if not isinstance(arr, list):
            raise ValueError("Provided array is not a list")
        # 选择排序算法
        sort_choice = request.query.sort_choice
        if sort_choice == 'bubble':
            sorted_arr = bubble_sort(arr.copy())
        elif sort_choice == 'quick':
            sorted_arr = quick_sort(arr.copy())
        else:
            return {"error": "Invalid sort choice"}
        return {"sorted_array": sorted_arr}
    except (SyntaxError, ValueError):
        return {"error": "Invalid input format"}

# 运行Bottle应用
if __name__ == '__main__':
    run(host='localhost', port=8080)