import random

def main():

    # Generate and print 10 random numbers between 1 and 100

    for _ in range(10):

        print(random.randint(1, 100), end=" ") # randint generate random number and end print in one line result


if __name__ == '__main__':
    main()
