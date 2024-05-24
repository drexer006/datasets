import argparse
import random
from opustools import OpusRead

def main(source, target, number):
    source_file = f"{source}-{target}.{source}"
    target_file = f"{source}-{target}.{target}"

    with open(source_file, "r", encoding="utf-8") as file:
        source_lines = file.readlines()

    with open(target_file, "r", encoding="utf-8") as file:
        target_lines = file.readlines()

    if len(source_lines) != len(target_lines):
        raise ValueError("Source and target lines do not match")

    max_start_index = len(source_lines) - number
    if max_start_index <= 0:
        start_index = 0
        end_index = number
    else:
        start_index = random.randint(0, max_start_index)
        end_index = start_index + number

    def truncate_file(file_path, start_index, end_index):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        selected_lines = lines[start_index:end_index]

        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(selected_lines)

    truncate_file(source_file, start_index, end_index)
    truncate_file(target_file, start_index, end_index)

    print("Files were truncated to the specified number of lines.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a sample from input files"
    )
    parser.add_argument("source", type=str, help="Source language file path")
    parser.add_argument("target", type=str, help="Target language file path")
    parser.add_argument("number", type=int, help="number of strings")
    args = parser.parse_args()

    main(args.source, args.target, args.number)
