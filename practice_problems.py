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
    product_set = set(product_ids)
    if list(product_set) == product_ids:
        return False
    else:
        return True
#This is an effective way to do this as a set cannot have repeated values and by comparing a set to the 
#original array, we can see if there are any duplicates 

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
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
        return removed_node.value
#This is the queue we learned last week. It was effective as a first-in, first-out
#system, which is what the assignment calls for. 

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
        self.things_to_track = []

    def add(self, value):
        self.things_to_track.append(value)

    def get_unique_count(self):
        return len(set(self.things_to_track))
#This uses a similar method to question 1, by converting it to a set, we can get only unique
#elements, making the number of unique elements the leingth of the set