i = int(0)

while i == 0:
    op = int(input("Choose a operation: \n1 - To calculate the distance between 2 dots \n2 - To identify if a dot is or not in the circunference \n3 - To exit \n\n"))

    if op >= 1 and op <= 3:
        if op == 1:
            print("\nPlease put the coordinates of the first dot: ")
            x1 = float(input("X: "))
            y1 = float(input("Y: "))
            print("\nPlease put the coordinates of the second dot: ")
            x2 = float(input("X: "))
            y2 = float(input("Y: "))

            distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
            
            print(distance, "\n\n")

        if op == 2:
            print("\nPlease put the circle radius valor: ")
            distance = float(input())
            print("\nPlease put the coordinates of the central dot: ")
            x1 = float(input("X: "))
            y1 = float(input("Y: "))
            print("\nPlease put a dot coordinates: ")
            x2 = float(input("X: "))
            y2 = float(input("Y: "))
            
            if ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) == distance:
                print("\nIts a dot of the circunference!\n")

            else:
                print("\nIts not a dot of the circunference!\n")

        if op == 3:
            print("\nExiting...\n\n")
            break


    else:
        print("Please chosse a valid operator!\n\n")
