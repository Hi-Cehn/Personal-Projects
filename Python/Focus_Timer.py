import time

def timer():
    print("Would you like to start the timer?")
    print("Enter Yes to start, or any other key to stop the program.")
    choice = input("Enter your choice here: ")

    option(choice)

def option(choice):
    if choice == "Yes":
        print("Timer started.")

        start = time.time_ns() / 1000000000

        while True:
            current = time.time_ns() / 1000000000

            if current - start >= 5:
                print("Time's up.")
                quit()
    else:
        quit()

if __name__ == "__main__":
    timer()