x=int(input(""))
z=x%100
y=x//100
if y>12:
    y=y-12
    print(f"{y}:{z:02d} pm")
else:
    print(f"{y}:{z:02d} am")
