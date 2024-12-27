#Chuong trinh chinh
ans = True
while ans:
    print("1. Hinh tron")
    print("2. Hinh vuong")
    print("3. Hinh chu nhat")
    print("4. Ket thuc")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        #Hinh tron
        def area(r):
            return pi*r*r
        def perimeter(r):
            return 2*pi*r

        pi = 3.14

        r = float(input("Enter the radius: "))

        print(f'The area of cirle is: {area(r)}')
        print(f'The perimeter of cirle is: {perimeter(r)}')

    elif choice == 2:
        #Hinh vuong
        def area(c):
            return c*c
        def perimeter(c):
            return 4*c

        
        c = float(input("Enter the side: "))

        print(f'The area of square is: {area(c)}')
        print(f'The perimeter of square is: {perimeter(c)}')

    elif choice == 3:
        #Hinh chu nhat
        def area(a,b):
            return a * b
        def perimeter(a, b):
            return 2 * (a + b)

        a = float(input("Enter the length: "))
        b = float(input("Enter the width: "))

        print(f'The area of rectangle is: {area(a,b)}')
        print(f'The perimeter of rectangle is: {perimeter(a,b)}')

    elif choice == 4:
        print("Goodbye")
        break
    elif choice < 1 or choice > 4:
        print("Invalid choice. Please try again.")


