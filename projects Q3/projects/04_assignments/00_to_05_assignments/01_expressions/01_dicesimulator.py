import random


def roll_dice():
    die_1:int = random.randint(1,6)
    die_2:int = random.randint(1,6)
    total = die_1 + die_2
    print(f"total of two dies : {total}")


def main():
    die_1:int = 10
    print("Die1 in main() start as :" + str(die_1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Die1 in main() is :" + str(die_1))


if __name__ == "__main__":
    main()