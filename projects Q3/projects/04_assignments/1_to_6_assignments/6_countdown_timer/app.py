import time



try:
    countdown_time = int(input("How many seconds do you want to count down from? "))

except Exception as error:
    print(error)
    exit()

while countdown_time > 0:
    minutes, seconds = divmod(countdown_time, 60)
    timer = f"{minutes:02d}:{seconds:02d}"
    print(timer, end="\r")
    time.sleep(1)
    countdown_time -= 1

print("Time's up!")

