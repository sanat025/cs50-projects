from cs50 import get_string

def main():
    text = get_string("Text: ")

    letters = 0
    words = 0
    sentences = 0

    for ch in text:
        if ch.isalpha():
            letters += 1
        elif ch in [".", "!", "?"]:
            sentences += 1

    word = len(text.split())

    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()

