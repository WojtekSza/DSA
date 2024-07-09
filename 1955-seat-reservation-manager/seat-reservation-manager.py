import heapq
class SeatManager:
    def __init__(self, n: int):
        self.heap=[]
        self.heap_set=set()
        for i in range(n):
            self.heap.append(i+1)
        print(self.heap)
    def reserve(self) -> int:
        if self.heap:
            removed=heapq.heappop(self.heap)
            self.heap_set.add(removed)
            return removed
    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.heap_set:
            heapq.heappush(self.heap,seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)