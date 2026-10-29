#лінійний пошук
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #повертаємо індекс елемента, якщо знайдено  
    return -1 #якщо не знайдено то повертаємо -1


arr = [10, 25, 30, 45, 50]
target = 30
result = linear_search(arr, target)
print(f"Index of {target}: {result}")
target = 90
result = linear_search(arr, target)
print(f"Index of {target}: {result}")

#бінарний пошук
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid #повертаємо індекс елемента, якщо знайдено
        elif arr[mid] < target:
            left = mid + 1 #переходимо до правої половини
        else:
            right = mid - 1 #переходимо до лівої половини
    return -1 #якщо не знайдено то повертаємо -1

arr = [5, 10, 15, 20, 25, 30, 35]
target = 20
result = binary_search(arr, target)
print(f"Index of {target}: {result}")
target = 40
result = binary_search(arr, target)
print(f"Index of {target}: {result}")