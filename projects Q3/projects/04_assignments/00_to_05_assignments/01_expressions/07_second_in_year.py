
days_in_year :int = 365
houres_per_day : int = 24
minutes_per_houres : int = 60
seconds_per_minutes :int = 60

def seconds():
    print(f"There are {days_in_year * houres_per_day * minutes_per_houres * seconds_per_minutes} seconds in a year ")

if __name__ == "__main__":
    seconds()