import os


POEM = (
    "The inventory bot marks\n"
    "the brass key: discard.\n"
    "The shed came down in April.\n"
    "\n"
    "I lift it from the bench\n"
    "and add it to my ring.\n"
    "All day it knocks\n"
    "against the key I use."
)

if not 1 <= len(POEM) <= 1000 or not POEM.strip():
    raise ValueError("POEM must contain 1-1,000 characters and at least one non-space character")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(POEM)


if __name__ == "__main__":
    main()
