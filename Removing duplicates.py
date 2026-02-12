x = [7,2,7,1,2,2,0,0,4,1,1,1,1,2,0,0,7,9,6,9,8,3]
y = []
for num in x:
    if num not in y:
        y.append(num)
print("Original list:", x)
print("New list:", y)


OUTPUT
Original list: [7, 2, 7, 1, 2, 2, 0, 0, 4, 1, 1, 1, 1, 2, 0, 0, 7, 9, 6, 9, 8, 3]
New list: [7, 2, 1, 0, 4, 9, 6, 8, 3]
