def triangle():
    print("This code is about sum of triangle sides")

    side_1:float = float(input("Enter your first side no of triangle. "))
    side_2:float = float(input("Enter your second side no of triangle. "))
    side_3:float = float(input("Enter your third side no of triangle. "))
    total:float = float(side_1 + side_2 + side_3)
    print(f"The perimeter of the triangle is {total}")


if __name__ == "__main__":
    triangle()