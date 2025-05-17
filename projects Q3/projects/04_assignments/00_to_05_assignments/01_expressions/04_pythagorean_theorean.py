import math

def triangle():
    ab:float = float(input("Enter the lenght of side ab : "))
    ac:float = float(input("Enter the lenght of side ac : "))
    bc:float = math.sqrt(ab ** 2 + ac **2)
    print(f"The lenght of bc (The hypothanuse is : {bc})")

if __name__ == "__main__":
    triangle()