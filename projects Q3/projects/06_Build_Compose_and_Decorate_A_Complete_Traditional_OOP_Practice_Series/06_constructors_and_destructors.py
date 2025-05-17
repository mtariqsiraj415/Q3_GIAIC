class Logger:
    def __init__(self):
        print("Logger Oject created")

    def __del__(self):
        print("Logger Object destroyed.")


log_1:Logger = Logger()
print(log_1)