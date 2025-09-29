"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):

    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Data Structure Choice: Set
# Reason: A set allows for very fast lookups (O(1) average time complexity).
# We use it to track IDs seen so far so we can detect duplicates efficiently.
# This gives an overall runtime of O(n), where n is the number of product IDs. 
"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
       
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if self.tasks: 
            return self.tasks.popleft()
        return None

# Data Structure Choice: deque (double-ended queue)
# Reason: deque allows O(1) time insertion at the end and removal from the front,
# which is exactly what a queue needs for efficient FIFO operations.
"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
 
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)



if __name__ == "__main__":
    print("Testing Problem 1:")
    print(has_duplicates([10, 20, 30, 20, 40]))  
    print(has_duplicates([1, 2, 3, 4, 5]))      

    print("\nTesting Problem 2:")
    tq = TaskQueue()
    tq.add_task("Email follow-up")
    tq.add_task("Code review")
    print(tq.remove_oldest_task())  
    print(tq.remove_oldest_task())  
    print(tq.remove_oldest_task())  

    print("\nTesting Problem 3:")
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())  # 2

# Data Structure Choice: set
# Reason: A set automatically stores only unique values,
# so checking and storing values is fast (O(1) average time).
# This allows O(1) time retrieval of the count of unique values.



