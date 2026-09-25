import csv
import os
import re

INPUT_DIR = os.path.join("data", "shakespeare")
STOPWORDS_PATH = os.path.join(INPUT_DIR, "stopwords.txt")
SHAKESPEARE_PATH = os.path.join(INPUT_DIR, "shakespeare.txt")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "shakespeare_report.csv")

NUM_LINES_TO_SKIP = 246
LAST_LINE_START = "End of this Etext"


def load_stopwords():
    """Load the stopwords from the file and return a set of the cleaned stopwords."""

    stopwords = set()

    with open(STOPWORDS_PATH, encoding="utf-8") as file:
        text=file.read().lower()

    clean_text=re.sub(r"[^A-Za-z\s]", "", text)
    clean_text=re.sub(r"\s+", " ", clean_text)
    stopwords=set(clean_text.split())

    return stopwords


def load_shakespeare_lines():
    "Loads every line in the dataset that was written by Shakespeare as a list of strings."

    shakespeare_lines = []

    in_attribution = False

    with open(SHAKESPEARE_PATH, encoding="utf-8") as file:
        for line_number, line in enumerate(file):
            if line_number<NUM_LINES_TO_SKIP:
                continue

            if line.startswith(LAST_LINE_START):
                break

            if line.lstrip().startswith("<<"):
                in_attribution=True

            if not in_attribution:
                shakespeare_lines.append(line)

            if in_attribution and ">>" in line:
                in_attribution=False

    return shakespeare_lines


def get_shakespeare_words(shakespeare_lines):
    """Takes the lines and makes a list of lowercase words."""

    text="".join(shakespeare_lines)
    text=text.lower()
    text=re.sub(r"[^A-Za-z\s]", "", text)
    text=re.sub(r"\s+", " ", text)
    words=text.split()

    return words


def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""

    word_counts = dict()

    for word in words:
        if word not in stopwords:
            if word in word_counts:
                word_counts[word]=word_counts[word]+1
            else:
                word_counts[word]=1

    return word_counts


def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by count in descending order."""

    sorted_word_counts=sorted(
        word_counts.items(),
        key=lambda pair: pair[1],
        reverse=True
    )

    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""

        with open(path, "w", newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(["word", "count"])

        for word, count in sorted_word_counts:
            writer.writerow([word, count])


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stopwords = load_stopwords()

    shakespeare_lines = load_shakespeare_lines()
    shakespeare_words = get_shakespeare_words(shakespeare_lines)

    word_counts = count_words(shakespeare_words, stopwords)
    word_counts_sorted = sort_word_counts(word_counts)

    write_word_counts(word_counts_sorted, OUTPUT_PATH)
