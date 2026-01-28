x=int(input(""))
z=x%100
y=x//100
if x==2400:
    print("00:00 am")
elif y>12:
    y=y-12
    print(f"{y}:{z:02d} pm")
else:
    print(f"{y}:{z:02d} am")


OUTPUT
2355
11:55 pm
