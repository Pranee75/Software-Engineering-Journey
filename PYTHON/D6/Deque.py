# Sliding Window Maximum

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # Stores indices
    result = []
    
    for i, num in enumerate(nums):
        # 1. Remove indices out of current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 2. Remove elements smaller than current from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()
            
        dq.append(i)
        
        # 3. Add to result once the first window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  


# Palindrome Checker

from collections import deque

def is_palindrome(s):
    # Filter non-alphanumeric and normalize
    chars = deque(c.lower() for c in s if c.isalnum())
    
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  


# Circular Deque Implementation

class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertLast(self, value):
        if self.size == self.k: return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self):
        if self.size == 0: return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

print(MyCircularDeque(3).insertLast(1))  # True
print(MyCircularDeque(3).insertLast(2))  # True

