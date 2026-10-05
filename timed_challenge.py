# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""
2. Running Total with Reset
Track a running total of values. If a negative number is added, reset the total to 0.
Input: [5, 7, -1, 3, 2]
Output: [5, 12, 0, 3, 5]
"""

def running_total(values):
    if len(values) == 0:
        return "Error parsing: Empty list"
    total = 0
    total_list = []
    for value in values:
        try:
            if int(value) < 0:
                total = 0
            else:
                total += int(value)
            total_list.append(total)
        except:
            return "Error parsing: Non-number values"
    return total_list

val_input = [5, 7, -1, 3, 2]
print(running_total(val_input))

val_input = []
print(running_total(val_input))

val_input = [5, 7, "Hello", 3, 2]
print(running_total(val_input))