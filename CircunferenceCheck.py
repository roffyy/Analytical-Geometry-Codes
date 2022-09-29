centerX = float(input("Put the value of X (Center of Circunference): "))
centerY = float(input("Put the value of Y (Center of Circunference): "))
radius = float(input("Put the circunference radius value: "))
x = float(input("Put a value for a dot (X Axis): "))
y = float(input("Put a value for a dot (Y Axis): "))

distance = ((x - centerX)**2 + (y - centerY)**2)**(1/2)

if distance <= radius:
    print("\nThe dot is in the circunference\n")

else:
    print("\nThe dot isnt in the circunference\n")

