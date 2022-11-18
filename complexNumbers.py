def finalResult(a, b, bi):
    if type(bi) == str:
        if bi == "i":
            print(f"The final result is: {a} + {b}i")
        else:
            print(f"The final result is: {a} - {b}i")
    else:
        print(f"The final result is: {a + bi}")

def imaginaryNumber(b, i):
    if i % 4 == 0: return b
    if i % 4 == 1: return "i"
    if i % 4 == 2: return -b
    if i % 4 == 3: return "-i"

def userInput():
    try:
        a, b = (input("Type a complex number (format example: a + bi^2): ")).split(" + ")
    except:
        print("Incorrect Format!")
        return userInput()

    try:
        b, i = b.split("i^")
        a, b, i = float(a), float(b), float(i)
        return a, b, i
    except:
        print("Type a valid complex number!")
        return userInput()

def main():
    a, b, i = userInput()
    bi = imaginaryNumber(b, i)
    finalResult(a, b, bi)

main()