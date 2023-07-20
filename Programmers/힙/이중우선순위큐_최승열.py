import heapq as hq

class DeapQ():
    minHeap = []
    maxHeap = []
    size = 0
    
    def insert(self, num):
        self.size += 1
        hq.heappush(self.minHeap, num)
        hq.heappush(self.maxHeap, -num)
    
    def delete(self, num):
        if self.size == 0: return
    
        tg = self.maxHeap if num == 1 else self.minHeap
        
        hq.heappop(tg)
        self.size -= 1
        
        if not self.size:
            self.minHeap.clear()
            self.maxHeap.clear()
    
    def getMax(self):
        return -self.maxHeap[0] if self.maxHeap else 0
    
    def getMin(self):
        return self.minHeap[0] if self.minHeap else 0
    
    
def solution(operations):
    dq = DeapQ()
    
    for o in operations:
        command, num = o.split()
        num = int(num)
        
        if command == "I": dq.insert(num)
        else: dq.delete(num)
    
    return [dq.getMax(), dq.getMin()]