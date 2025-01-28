def word_counter(word):
    words = word.split()
    word_counts = {}
    for i in words:
        i = i.lower()
        word_counts[i] = word_counts.get(i,0) + 1
    return word_counts
user_sentence = input("enter a sentence:")
result = word_counter(user_sentence)
print("word occurences")
for i, count in result.items():
    print(f"{i}:{count}")
def main():
    word_counter(i)
main()