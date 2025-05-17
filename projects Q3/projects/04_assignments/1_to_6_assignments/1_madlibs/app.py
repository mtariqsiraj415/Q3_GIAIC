
def mad_libs():

    name = str(input("Enter your name : "))
    programing_language = str(input("Enter a programming language : "))
    mentor = str(input("Enter your mentor name : "))
    location = str(input("Enter location : "))




    # Story created  3 type to print the story


    # 1st type



    print("\n Here is little story based on mad libs game!")
    print(f"Oncae upon a time, there was a named {name}.")
    print(f"{name} was very curious and always want to learn new things.")
    print(f"One day, He/She decided to learn {programing_language} language at {location}.")
    print(f"Luckily {name} found a greater mentor name as {mentor} who was an expert in {programing_language}.")


if __name__ == "__main__":
    mad_libs()




# 2nd type

'''

print("\n Here is little story based on mad libs game!")
print("Oncae upon a time, there was a named "+ name +".")
print(name +"was very curious and always want to learn new things.")
print("One day, He/She decided to learn "+ programing_language+ " language at " +location +".")
print("Luckily " + name +" found a greater mentor name as " +mentor+" who was an expert in " +programing_language+ ".")
print("\n")


'''





# 3rd type

'''
print("\n Here is little story based on mad libs game!")
print("Oncae upon a time, there was a named {}." .format(name))
print("{} was very curious and always want to learn new things.".format(name))
print("One day, He/She decided to learn {} language at {}.".format(programing_language, location))
print("Luckily {} found a greater mentor name as {} who was an expert in {}.".format(name, mentor, programing_language))
print("\n")

'''