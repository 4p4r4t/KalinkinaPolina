import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=","))

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
