n = int(input(""))
f= 1
i = 1
while i <= n:
    if i == 1:
        i += 1
        continue
    f*= i
    i += 1
print(f)


OUTPUT
5
120
