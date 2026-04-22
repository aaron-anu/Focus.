import os
from profile import run

import lib.tasks as ts


def main():
    print("Initializing")

    # create data dir
    data_dir = os.path.dirname(os.path.abspath(__file__)) + "/../data"
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    running = True
    while running:
        print("""1. Add tasks
2. List tasks
3. Mark as done
4. Start timer
*. Exit""")
        choice = input("Enter choice: ")
        match choice:
            case _:
                running = False
                print("Exiting...")


if __name__ == "__main__":
    main()
