def count_stats(text):
    words = text.split()
    characters = len(text.replace(" ", ""))
    sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]

    return {
        "words": len(words),
        "characters": characters,
        "sentences": len(sentences)
    }


def main():
    print("=== Word Counter ===")
    text = input("Enter a paragraph:\n")

    stats = count_stats(text)

    print("\n--- Results ---")
    print(f"Words     : {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print(f"Sentences : {stats['sentences']}")


if __name__ == "__main__":
    main()