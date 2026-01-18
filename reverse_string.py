def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    text = input("Enter text: ")
    print("Reversed:", reverse_text(text))