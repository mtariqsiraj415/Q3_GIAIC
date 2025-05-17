def temp():
    print("This code for converting fahrenheit to celsius")
    fahrenheit_degree = float(input("Enter your fahrenheit degree :"))
    celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
    print(f"Tempereture {fahrenheit_degree}f = {celsius_degree}c")

if __name__ == "__main__":
    temp()