marks = [78, 85, 62, 90, 88, 76, 95, 69]
avg = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)
c = 0
for mark in marks:
    if mark > average:
        c += 1
print("Average:", avg)
print("Highest:", highest)
print("Lowest:", lowest)
print("Above avg:", c)
