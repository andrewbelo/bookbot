def count_letter_frequencies(text):
    frequencies = {}
    for letter in text.lower():
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies


def count_words(text):
    return len(text.split())


def print_report(text):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{count_words(text)} words found in the document\n\n"
    frequencies = count_letter_frequencies(text)
    for letter, frequency in sorted(
        frequencies.items(), key=lambda item: item[1], reverse=True
    ):
        if letter.isalpha():
            report += f"The '{letter}' character was found {frequency} times\n"
    report += "--- End report ---"
    return report


if __name__ == "__main__":
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()
        # print(text)
        print(count_words(text))
        print(count_letter_frequencies(text))
