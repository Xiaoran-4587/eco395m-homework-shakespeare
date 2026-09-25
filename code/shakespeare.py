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

    # fill this in

    return stopwords


def load_shakespeare_lines():
    "Loads every line in the dataset that was written by Shakespeare as a list of strings."

    shakespeare_lines = []

    # fill this in

    return shakespeare_lines


def get_shakespeare_words(shakespeare_lines):
    """Takes the lines and makes a list of lowercase words."""

    # fill this in

    return words


def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""

    word_counts = dict()

    # fill this in

    return word_counts


def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by count in descending order."""

    # fill this in

    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""

       # fill this in


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stopwords = load_stopwords()

    shakespeare_lines = load_shakespeare_lines()
    shakespeare_words = get_shakespeare_words(shakespeare_lines)

    word_counts = count_words(shakespeare_words, stopwords)
    word_counts_sorted = sort_word_counts(word_counts)

    write_word_counts(word_counts_sorted, OUTPUT_PATH)
