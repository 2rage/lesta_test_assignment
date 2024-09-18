# 1 task

def isEven(value):
    if value % 2:
        return False
    return True


print(isEven(10))  # True
print(isEven(7))   # False


# 2 task

class RingBuffer:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def add(self, item):
        if self.size == self.capacity:
            raise OverflowError("буфер достиг своей максимальной емкости")
        self.data[self.end] = item
        self.end = (self.end + 1) % self.capacity
        self.size += 1

    def remove(self):
        if self.size == 0:
            raise IndexError("буфер пустой")
        item = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


buffer = RingBuffer(3)
buffer.add(5)
buffer.add(10)
buffer.add(15)
print(buffer.remove())
buffer.add(20)
print(buffer.remove())
print(buffer.is_full())


# 3 task

# Использовал итеративный подход, чтобы избежать глубоких рекурсивных вызовов, которые могут привести к переполнению стека при больших объемах данных

def iterative_quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [33, 2, 52, 106, 73, 2, 45]
sorted_arr = iterative_quick_sort(arr)
print(sorted_arr)
