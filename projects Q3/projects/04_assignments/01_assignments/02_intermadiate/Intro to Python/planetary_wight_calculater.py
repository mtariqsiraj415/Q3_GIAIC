def main():
     
     print("********************** Wellcome to the Planetary Wight Calculater **********************")

     earth_wight = float(input("Enter your wight on Earth : "))
     gravity_rations = {
            "Mercury" : 0.14 , 
            "Vanus"  : 0.9 ,
            "Mars" : 0.8 ,
            "Jupiter" : 2.34 ,
            "Saturn" : 1.06 ,
            "Uranas" : 0.92 ,
            "Neptune" : 1.19 
            }
        
        
        
     print("\n Select a planet")
     for i in gravity_rations:
        print(f"{i}")

     planet_choice = input("Enter the name of the planet :").title()
     if planet_choice in gravity_rations:
        new_wight = earth_wight * gravity_rations[planet_choice]
        print(f"Your wight on {planet_choice} is {new_wight}kg")
     else:
        print("Invalid name Choice")

if __name__ == "__main__":
     main()
