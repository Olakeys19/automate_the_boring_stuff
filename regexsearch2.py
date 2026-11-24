#TODO: Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.

import os
import re


def main():
    folder = input("Enter folder path: ").strip() or "."
    pattern = input("Enter regular expression: ")
    regex = re.compile(pattern)

    with os.scandir(folder) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.endswith(".txt"):
                continue

            try:
                with open(entry.path, "r", encoding="utf-8", errors="replace") as file:
                    for line_number, line in enumerate(file, 1):
                        if regex.search(line):
                            print(f"{entry.path}:{line_number}: {line}", end="")
            except OSError as error:
                print(f"Could not read {entry.path}: {error}")


if __name__ == "__main__":
    main()


                
                
                