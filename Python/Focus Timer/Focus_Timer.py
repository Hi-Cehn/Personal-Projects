import time
import keyboard

def timer():
    print("Would you like to start the timer?")
    print("Enter Yes to start, or any other key to stop the program.")
    choice = input("Enter your choice here: ")

    option(choice)

def time_translate(count):
    format = time.strftime("%H:%M:%S", time.gmtime(count))

    return format

def option(choice):
    if choice == "Yes":
        print("Timer started.")
        print("Press the q key on your keyboard to stop the timer.")

        start = time.time()

        exit_flag = True

        count = 5

        try:
            while count:
                timer = time_translate(count)
                print("\r" + str(timer), end="")

                current = time.time()

                if current - start >= 1:
                    count -= 1

                    start = current

                if keyboard.is_pressed("q"):
                    exit_flag = False
                    break

                time.sleep(0.1)

        finally:
            keyboard.clear_all_hotkeys()
            keyboard.unhook_all()

        if exit_flag:
            print("\rTime's up.")
        else:
            print("\nYou have stopped the system. Goodbye.")

        quit()
    else:
        quit()

if __name__ == "__main__":
    timer()