import re

from cs50 import get_string


def main():
    # Getting text
    Text = get_string("Text: ")

    # Analizing text
    nLetters = count_letters(Text)
    nWords = count_words(Text)
    nSentences = count_sentences(Text)

    L = nLetters * 100.0 / nWords
    S = 100.0 / nWords * nSentences

    GradeF = 0.0588 * L - 0.296 * S - 15.8
    # Rounding and converting into int
    Grade = int(round(GradeF))

    # Printing the calculated grade
    if Grade < 1:
        print("Before Grade 1")
    elif Grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {Grade}")


def count_letters(Text):
    # Counting alphabetic letters
    nLetters = 0
    for c in Text:
        if c.isalpha():
            nLetters += 1

    return nLetters


def count_words(Text):
    # Counting words divided by spaces
    nWords = 0
    if not count_letters(Text) == 0:
        nWords = 1
        for c in Text:
            if c.isspace():
                nWords += 1

    return nWords


def count_sentences(Text):
    # Counting sentences, ended with . ! ?
    nSentences = 0
    if not count_letters(Text) == 0:
        for c in Text:
            if c in ["!", ".", "?"]:
                nSentences += 1

    return nSentences


if __name__ == "__main__":
    main()