import os
from datetime import datetime
from keyword import iskeyword

import pandas as pd

import lib.tasks as ts

df = pd.read_csv("")

# (id, title, birthtime, duetime, done, desc)


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
            case "1":
                tit = input("Enter title of task: ")
                desc = input("Enter desc of task: ")
                due = input("Enter duetime of task: ")
                birthtime = datetime.now()
                done = False

            case "2":
                print("aaaaaa")
            case "3":
                tit = input("Enter the title of task completed: ")
                if (df["title"] == tit).any():
                    df.loc[df["title"] == tit, df.columns[4]] = True
                    print("Task marked as completed")
                else:
                    print("No matching title found")

            case 4:
                print("aaaaaa")
            case _:
                running = False
                print("Exiting...")


if __name__ == "__main__":
    main()
