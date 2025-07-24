# Simple Language Translator

A Python script that translates words into multiple languages using the `translate` library.  
Users select a target language code, enter a word, and receive the translation.  
Translations are also saved to a `Translation.txt` file for later reference.

---

## Features

- Supports translation to Spanish, Portuguese, Japanese, Korean, and Chinese
- Interactive command-line interface for language and word input
- Saves all translations to a text file
- Basic error handling for translation failures and file writing

---

## Requirements

- Python 3.x  
- `translate` Python package

Install the required package via pip:

```bash
pip install translate
```

---

## Usage

Run the script:

```bash
python script.py
```

Follow prompts to:

1. Choose a language code (e.g. `es` for Spanish)  
2. Enter the word you want to translate

The translated word will be displayed and saved to `Translation.txt`.

---

## Notes

- If the script cannot save to the file, it will notify you and raise an error.  
- Supported languages and their codes:

| Code | Language   |
|-------|------------|
| es    | Spanish    |
| pt    | Portuguese |
| ja    | Japanese   |
| ko    | Korean     |
| zh    | Chinese    |

---

