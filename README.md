# MASSIVEDATASET README

## Introduction

This project focuses on processing and managing language data. It answers two main questions:

1. **Python3 Development Environment Setup:** Set up a Python3 development environment, install relevant dependencies, and build a project structure similar to PyCharm's. Import a massive dataset and generate language-specific Excel files (en-xx.xlsx) using specific fields (id, utt, and annot_utt). Recursive algorithms are not used to optimize performance.

2. **Working with Files:** Generate separate JSONL files for English (en), Swahili (sw), and German (de) datasets with test, train, and dev partitions. Create a single large JSON file showcasing translations from English to other languages (xx) for the training dataset.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

## Installation

You can install the required Python libraries/packages using the following command:

```
pip install jsonlines json os pandas sys
```

```
pip install json
```

```
pip install os
```

```
pip install pandas
```

```
pip install sys
```


## Project Structure

The project structure should resemble the following:

```
project-root/
│
├── 1.1/data/
│       └── excel
│
├── main.py
├── q2.py
│
│
├── en-xx.xlsx (Generated)
├── en_train.jsonl (Generated)
├── sw_train.jsonl (Generated)
├── de_train.jsonl (Generated)
│   └── translations.json (Generated)
│
├── README.md
├── generator.sh
└── other_files...
```

## Running the Project

Question 1

Place your dataset file (input_data.xlsx) inside the data/ directory.

Run the following command to execute Question 1:

```
./generate.sh
```

The script will generate language-specific Excel files (en-xx.xlsx) in the results/ directory.

Question 2

Make sure you have the English (en), Swahili (sw), and German (de) JSONL files (e.g., en-US.jsonl, de-DE.jsonl, sw-KE.jsonl) in the project directory.

Run the following command to execute Question 2(shell command):

```
python q2.py
```

The script will generate separate JSONL files for English, Swahili, and German in the results/ directory. Additionally, it will create a large JSON file (translations.json) showcasing translations from English to other languages.


Run the following command to upload files to google drive:

```
python googledrive.py
```
