import time
start_time = time.time()


def main():
    n = 0
    while n < 1000000000:
        n += 1
        print(n)
    if n == 1000000000:
        print("1 billion")


main()
print("--- %s seconds ---" % (time.time() - start_time))
