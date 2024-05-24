import argparse
import os
from datasets import load_dataset

MODELS = [
    "opus100",
    "opus_books",
    "kde4",
]

def list_models():
    print("Available models:")
    print("\n".join(MODELS))

def main(model_name, lang1, lang2, start_index, end_index):
    if model_name in ["opus", "opus-books"]:
        dataset = load_dataset(model_name, f"{lang1}-{lang2}")
    elif model_name == "kde4":
        dataset = load_dataset("kde4", lang1=lang1, lang2=lang2)

    dataset = dataset.shuffle()

    sample_dataset = dataset['train'].select(range(start_index, end_index))

    with (
        open(f"{lang1}.txt", "w", encoding="utf-8") as lang1_file,
        open(f"{lang2}.txt", "w", encoding="utf-8") as lang2_file
    ):
        # Iterate through the dataset and write source and target strings to files
        for example in sample_dataset:
            lang1_string = example['translation'][lang1]
            lang2_string = example['translation'][lang2]
            lang1_file.write(lang1_string + "\n")
            lang2_file.write(lang2_string + "\n")

    print("Files were generated")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate lang1.txt and lang2.txt files from huggingface datasets"
    )
    parser.add_argument(
        "model_name",
        type=str,
        choices=MODELS,
        help=f"Model name. Available options: {', '.join(MODELS)}"
    )
    parser.add_argument("lang1", type=str, help="First language")
    parser.add_argument("lang2", type=str, help="Second language")
    parser.add_argument("start_index", type=int, help="Start index of examples to select")
    parser.add_argument("end_index", type=int, help="End index of examples to select")
    args = parser.parse_args()

    main(args.model_name, args.lang1, args.lang2, args.start_index, args.end_index)
