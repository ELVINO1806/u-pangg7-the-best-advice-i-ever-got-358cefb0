import os, sys

ENTRY = "'Marry someone who laughs at your worst joke,' my aunt said, 'because one day that joke will be your whole life.'"
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main():
    if len(ENTRY) > MAX_CHARS:
        print("entry exceeds 200-character cap", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
