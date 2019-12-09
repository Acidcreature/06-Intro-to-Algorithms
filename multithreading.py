"""

Running things concurrently is known as multithreading
Running things in parallel is known as multi processing

I/O bound tasks - Waiting for input and output to be completed,
                  reading and writing from file system,
                  network operations,
                  These all benefit more from threading
                  You get the illusion of running code at the same time,
                    however other code starts running wile other code is waiting

CPU bound tasks - Good for number crunching
                    using CPU,
                    data crunching
                    These benefit more from multiprocessing and running in parallel
                    Using multiprocessing might be slower if you have overhead from
                    creating and destroying files


"""
import threading
import time
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done sleeping')

# create two threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# start the thread
t1.start()
t2.start()

# make sure the threads complete before moving on to calculate finish time
t1.join()
t2.join()

#do_something()
#do_something()

finish = time.perf_counter()

print(F"Finished in {finish - start} second(s)")