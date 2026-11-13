'''
Design a class that processes a stream of integers one at a time and supports two operations:

add(num), which records a new number, and 

hasPair(target), which returns True if any two numbers currently in the last W numbers added sum to target. 

Numbers that fall outside the most recent W adds no longer count.
W = 3
add(1)
add(5)
add(3)
hasPair(8)   -> True   # 5 + 3
add(9)   	# window is now [5, 3, 9]; the 1 has expired
hasPair(6)   -> False  # 1 + 5 no longer counts, 1 has expired
hasPair(12)  -> True   # 3 + 9
'''
from collections import deque, Counter

class WindowPairs:
    def __init__(self, w: int):
        self.w = w
        self.window = deque()
        self.counts = Counter()

    def add(self, num: int):
        self.window.append(num)
        self.counts[num] += 1

        if len(self.counts) > s.w:
            oldest = self.window.popleft()
            self.counts[oldest] -= 1
            if self.counts[oldest] == 0:
                del self.counts[oldest]

    def hasPair(self, target: int):
        for x, count in self.counts.items():
            partner = target - x
            if partner == x:
                if count >= 2:
                    return True
            elif partner in self.counts:
                return True

        return False

s = WindowPairs(3)
s.add(3)
s.add(4)
s.add(5)

print(s.hasPair(7))
