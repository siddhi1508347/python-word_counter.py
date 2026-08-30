# Word Counter

A simple Python command-line tool that analyzes a paragraph of text and returns basic statistics — word count, character count, and sentence count.

## Description

Word Counter takes user input as a paragraph and processes it to calculate:
- **Word count** — total number of words, split by whitespace
- **Character count** — total characters, excluding spaces
- **Sentence count** — number of sentences, detected using `.`, `!`, and `?` as delimiters

This project demonstrates basic string manipulation, text processing, and simple parsing logic in Python — no external libraries required.

## Features

- Lightweight, single-file script
- No dependencies — pure Python standard library
- Simple, readable code structure with a reusable `count_stats()` function
- Runs directly from the command line

## How to Run

```bash
python word_counter.py
```

You'll be prompted to enter a paragraph. The script will then display the word, character, and sentence counts.

## Example
=== Word Counter ===
Enter a paragraph:
Python is fun. Is it not? Yes, it is!

--- Results ---
Words     : 8
Characters: 30
Sentences : 3


## Tech Stack

- Python 3

## Possible Improvements

- Add average word length calculation
- Support reading input from a `.txt` file
- Add a GUI or web version (Flask/FastAPI)
