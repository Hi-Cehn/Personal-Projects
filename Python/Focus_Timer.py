import os
import time
import keyboard

def timer():
    print("Would you like to start the timer?")
    print("Enter Yes to start, or any other key to stop the program.")
    choice = input("Enter your choice here: ")

    option(choice)

def option(choice):
    if choice == "Yes":
        print("Timer started.")
        print("Press the q key on your keyboard to stop the timer.")

        start = time.time_ns() / 1000000000

        count = 5

        while count:
            print(count, end="\r")

            current = time.time_ns() / 1000000000

            if current - start >= 1:
                count = count - 1

                start = current

            if keyboard.is_pressed("q"):
                print("You have stopped the system. Goodbye.")
                quit()

        
        print("Time's up.")
        quit()
    else:
        quit()

if __name__ == "__main__":
    timer()