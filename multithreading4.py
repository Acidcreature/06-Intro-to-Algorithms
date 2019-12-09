"""
Prove that these are actually coming in as they are completed,
    lets pass in a range of seconds

start 5 second thread first but since we use as_completed() method, it prints
the results in the order that they are completed

"""
import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    
    seconds_list = [5, 4, 3, 2, 1]

    # list comprehension to create multiple threads
    results = [executor.submit(do_something, sec) for sec in seconds_list]

    # to get the results we can use another function from future object that gives
    # us and iterator
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(F"Finished in {finish - start} second(s)")