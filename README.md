# datasets
load datasets from [Hugging Face](https://huggingface.co/) and [Opus](https://opus.nlpl.eu/results/en&el/corpus-result-table)

## Run scripts

poetry install

cd load_datasets

-- Download dataset from huggingface for opus100 model, el, en languages and generate a file
with 500 sentences

poetry run python huggingface_main.py opus100 el en 0 500

- Download dataset from opus
poetry run python opus_main.py GlobalVoices en el

- Create a sample from generated files

poetry run pythonsample.py en el 500

