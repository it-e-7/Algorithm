import heapq

# 최대힙 구하기
def get_max_heap(iterable):
    heap = list(iterable)
    heapq.heapify(heap)
    return [-heapq.heappop(heap) for _ in range(len(heap))]

# 최소힙 구하기
def get_min_heap(iterable):
    heap = list(iterable)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

# 예시 사용
data = [4, 1, 7, 3, 8, 5]
print("Original data:", data)

max_heap = get_max_heap(data)
print("Max heap:", max_heap)

min_heap = get_min_heap(data)
print("Min heap:", min_heap)



