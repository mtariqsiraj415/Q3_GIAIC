def enerygy():
    c:int = 299792458
    m:int =  float(input("Enter kilos of mass : "))
    print(" e = m * c ^ 2")
    print("Mass = " +str(m)  + " kg")
    print("C = " + str(c) + " m/s")
    print("e = "+str(m * c ** 2) + " jules")

if __name__ == "__main__":
    enerygy()