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

Run 10 threads
We can also now pass in an argument for seconds

"""
import threading
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done sleeping')

# Initialize list of threads
threads = []

# loop to start 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

#do_something()
#do_something()

finish = time.perf_counter()

print(F"Finished in {finish - start} second(s)")