import argparse
from opustools import OpusRead

def main(model_name, source, target):
    source_file = f"{source}-{target}.{source}"
    target_file = f"{source}-{target}.{target}"

    OpusRead(
        directory=model_name,
        source=source,
        target=target,
        preprocess="moses",
        write=[f"{source_file}", f"{target_file}"]
    ).execute()

    print("Files were generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate lang1.txt and lang2.txt files from opus datasets"
    )
    parser.add_argument(
        "model_name",
        type=str,
    )
    parser.add_argument("source", type=str, help="Source language")
    parser.add_argument("target", type=str, help="Target language")
    args = parser.parse_args()

    main(args.model_name, args.source, args.target)
