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



#OUTPUT
case 1
create: hi
enter: hi
hello

case 2
create: g
enter: h
re-enter: h
re-enter: h
too many attempts
