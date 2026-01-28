x=input("create: ")
y=input("enter: ")
for i in range(0,3):
    if y==x:
        print("hello")
        break
    else:
        if i<2:
            y=input("re-enter: ")
        else:
            print("too many attempts")
