
 # -------------------------------- 2.Using Cls ------------------------------- #

class Counter:
    count = 0


    def __init__(self):
        Counter.count +=1


    @classmethod
    def dispay_count(cls):
        return f"Total Objects created : {cls.count}"
    
obj_1 : Counter = Counter()
obj_2 : Counter = Counter()
obj_3 : Counter = Counter()
print(Counter.dispay_count())


