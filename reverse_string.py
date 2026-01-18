import sys

def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    try:
        text = sys.argv[1]
    except IndexError:
        text = input("Enter text: ")

    print(reverse_text(text))
