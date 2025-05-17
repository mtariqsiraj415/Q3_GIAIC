import random

def dice():
    die_1:int = random.randint(1,6)
    die_2:int = random.randint(1,6)
    total:int = die_1 + die_2

    print(f"First Die : {die_1}")
    print(f"Second Die : {die_2}")
    print(f"Total of two dies  : {total}")


if __name__ == "__main__":
    dice()