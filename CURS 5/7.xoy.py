
x0 = 3
y0 = 3
width = 6
height = 6

user_x = int(input("Introduceti pe x\n"))
user_y = int(input("Introduceti pe y\n"))

# Varianta 1
if user_x > x0:
    if user_x < x0 + width:
        if user_y > y0:
            if user_y < y0 + height:
                print("Se afla in zona")
            else:
                print("Nu se afla in zona")
        else:
            print("Nu se afla in zona")
    else:
        print("Nu se afla in zona")
else:
    print("Nu se afla in zona")

# Varianta 2
if user_x > x0 and user_x < x0 + width and user_y > y0 and user_y < y0 + height:
    print("Se afla in zona")
else:
    print("Nu se afla in zona")

# Varianta 3
if x0 < user_x < x0 + width and y0 < user_y < y0 + height:
    print("Se afla in zona")
else:
    print("Nu se afla in zona")