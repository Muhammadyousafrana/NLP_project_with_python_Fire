[![CI](https://github.com/Muhammadyousafrana/NLP_project_with_python_Fire/actions/workflows/main.yml/badge.svg)](https://github.com/Muhammadyousafrana/NLP_project_with_python_Fire/actions/workflows/main.yml)
# NLP_project_with_python_Fire

## Overview

This project demonstrates the use of **Natural Language Processing (NLP)** techniques by leveraging popular Python libraries such as `wikipedia`, `textblob`, and `fire`. The main functionality is to extract and analyze noun phrases from Wikipedia articles via a simple command-line interface, orchestrated using the `fire` library.

## Features

- **Wikipedia Search & Summary**: Search for Wikipedia articles and fetch their summaries.
- **Noun Phrase Extraction**: Use TextBlob to extract meaningful noun phrases from Wikipedia article summaries.
- **Command-Line Interface**: Instantly access the main NLP functionality from the terminal using Python Fire.
- **Modular Codebase**: Core logic is separated in the `nlplogic` package for easy reuse and testing.
- **Testing, Linting, and Formatting**: Includes Makefile targets for automated testing, code linting, and formatting.

## Project Structure

```
.
├── nlplogic/
│   ├── __init__.py
│   └── corenlp.py         # Core NLP logic (Wikipedia search, summary, phrase extraction)
├── wikipedia_phrases.py   # CLI entry point using fire
├── test_corenlp.py        # Test for core functionality
├── requirements.txt       # Python dependencies
├── Makefile               # Automation for install, test, lint, and format
├── .gitignore
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammadyousafrana/NLP_project_with_python_Fire.git
   cd NLP_project_with_python_Fire
   ```

2. **Install dependencies and required corpora:**
   ```bash
   make install
   ```
   This will:
   - Upgrade pip
   - Install Python dependencies from `requirements.txt`
   - Download required text corpora for TextBlob

## Usage

### Command-Line Interface

Extract noun phrases from a Wikipedia article directly from the command line:

```bash
python wikipedia_phrases.py "<Wikipedia Search Term>"
```

**Example:**
```bash
python wikipedia_phrases.py "Microsoft"
```
This will output the noun phrases found in the summary of the "Microsoft" Wikipedia article.

### Programmatic Usage

You can also import and use the core logic in your own Python scripts:

```python
from nlplogic.corenlp import get_phrases

phrases = get_phrases("Microsoft")
print(phrases)
```

## Testing

Run tests using:

```bash
make test
```
or directly via pytest:
```bash
pytest -vv --cov=nlplogic test_corenlp.py
```

## Code Quality

- **Lint:** `make lint` (uses pylint)
- **Format:** `make format` (uses black)

## Dependencies

Main dependencies (see `requirements.txt` for full list):

- textblob
- wikipedia
- nltk
- pattern
- fire
- pytest, pytest-cov (for testing)
- black, pylint, click (for code quality and CLI)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Example Code

**nlplogic/corenlp.py** contains functions for:
- Searching Wikipedia
- Fetching article summaries
- Extracting noun phrases using TextBlob

**wikipedia_phrases.py** provides a CLI using Fire, exposing `get_phrases` for quick access.

## Contributing

Feel free to open issues or pull requests if you'd like to contribute or suggest improvements!
