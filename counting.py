# This program  prints the number of iterations for the problem sizes
# that double using a nested loop


problemSize = 1000

for count in range(50):
    number = 0
    # the start of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # end of algorithm
    print(f'{problemSize} - {number}')
    problemSize *= 2