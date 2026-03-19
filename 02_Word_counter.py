                                           # Word Counter Application

def word_counter(text):
    words = text.split()
    word_count = {}

    for word in words:
        clean_word = word.lower().strip('.,!?;"\'()[]{}')
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    char_count = len(text)

    vowels = "aeiou"
    vowel_count = 0
    for char in text.lower():
        if char in vowels:
            vowel_count += 1

    most_common = max(word_count, key=word_count.get)

    print("\n--- TEXT ANALYSIS ---")
    print(f"Total Characters: {char_count}")
    print(f"Total Words: {len(words)}")
    print(f"Total Vowels: {vowel_count}")
    print(f"Most Common Word: '{most_common}' ({word_count[most_common]} times)")

    print("\n--- WORD FREQUENCY ---")
    for word, count in word_count.items():
        print(f'"{word}": {count}')


input_text = input("Enter a paragraph of text:\n")
word_counter(input_text)
