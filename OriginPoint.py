coordX, coordY, coordZ = [], [], []
Xsum, Ysum, Zsum = 0, 0, 0

amount = int(input("How many dots would you like to compute? \n"))

for i in range(amount):
    print("\n\nDot number: ", i+1)
    X = float(input("Put the X axis valor: "))
    Y = float(input("Put the Y axis valor: "))
    Z = float(input("Put the Z axis valor: "))
    coordX.append(X)
    coordY.append(Y)
    coordZ.append(Z)
    Xsum += coordX[i]
    Ysum += coordY[i]
    Zsum += coordZ[i]

CentX = Xsum/amount
CentY = Ysum/amount
CentZ = Zsum/amount

print("\n\nThe origin point is in the X: ", CentX)
print("The origin point is in the Y: ", CentY)
print("The origin point is in the Z: ", CentZ)
