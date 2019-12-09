import time

def test1():
    
    testone = [1, 10, 100, 1000, 2000, 4000, 10000, 50000, 100000, 1000000, 10000000, 100000000]
    start = time.process_time()
    for t in testone:
        count = 0
        while t > 0:
            t = t // 2
            count += 1
        print(count)
    print(start)
test1()
        